#!/usr/bin/env python

import pytest
import apps
from data.large_dataset import Environment
from data.large_dataset import Content
from data.assert_response import *
from tests.aeolus2 import Aeolus_Test
import time

class TestContent(Aeolus_Test):
    '''
    Create images, build, push, launch
    '''

    def test_create_images(self, mozwebqa):
        '''
        Create component outlines from images
        '''
        page = self.aeolus.load_page('Aeolus')
        page.login()

        for cloud in Environment.clouds:
            for image in Content.images:
                page.new_image_from_url(cloud['name'], image)

    def test_build_images(self, mozwebqa):
        '''
        Build images
        '''
        page = self.aeolus.load_page('Aeolus')
        page.login()
        
        for cloud in Environment.clouds:
            for image in Content.images:
                page.build_image(cloud['name'], image['name'])

    def test_push_images(self, mozwebqa):
        '''
        Push images
        '''
        page = self.aeolus.load_page('Aeolus')
        page.login()

        for cloud in Environment.clouds:
            for image in Content.images:
                # 'while not' used to loop until image built
                # FIXME: better way?
                while not page.verify_image_build(cloud['name'], image['name']):
                    time.sleep(30)
                else:
                    page.push_image(cloud['name'], image['name'])

    def test_create_blueprint(self, mozwebqa):
        '''
        create custom blueprints if defined in dataset
        otherwise the default blueprint is created
        '''
        page = self.aeolus.load_page('Aeolus')
        page.login()

        for catalog in Content.catalogs:
            for dataset_img in Content.images:
                deployable = "%s-%s" % (dataset_img['name'], \
                    catalog['cloud_parent'])
                if dataset_img['blueprint'] == "":
                    # default blueprint
                    page.new_default_blueprint(catalog['cloud_parent'],\
                        dataset_img, deployable)
                else:
                    # custom blueprint, get image uid from api
                    login = page.get_login_from_config('admin')
                    api_images = self.api.get_image_list(\
                        login['username'], login['password'])
                    for api_img in api_images:
                        if dataset_img['name'] == api_img['name']:
                            if catalog['cloud_parent'] == api_img['env']:
                                blueprint_file = \
                                    page.create_custom_blueprint(api_img, \
                                        dataset_img)
                                page.upload_custom_blueprint(blueprint_file, \
                                    catalog['name'], api_img, \
                                    dataset_img, deployable)

    @pytest.mark.skipif("1 == 1")
    def test_launch_configserver(self, mozwebqa):
        '''
        Launch configserver
        '''
        page = self.aeolus.load_page('Aeolus')
        page.login()

        for catalog in Content.catalogs:
            for image in Content.images:
                if image['name'] == "ConfigServer":
                    app_name = "%s-%s" % \
                        (image['name'], catalog['cloud_parent'])
                    page.launch_app(catalog['name'], app_name, image)
                    # TODO: configure via cli, ssh...

    # Manual steps required: configure config server
    # if ec2 get key, chmod
    # ssh
    # `aeolus-configserver-setup`, 'y', default, grab consumer key and secret
    # nav to cloud provider account, enter url, key, secret, assert notification

    @pytest.mark.skipif("1 == 1")
    def test_add_configserver(self, mozwebqa):
        '''
        Add configserver to enabled provider accounts
        '''
        page = self.aeolus.load_page('Aeolus')
        page.login()

        creds = page.get_credentials_from_config('configserver_credentials')
        for cloud in Environment.clouds:
            assert page.add_configserver_to_provider(cloud, creds) == \
                aeolus_msg['add_configserver']

    def test_launch_apps(self, mozwebqa):
        '''
        Launch apps.
        '''
        page = self.aeolus.load_page('Aeolus')
        page.login(role="user")

        # TODO: link catalogs and images more elegantly
        for catalog in Content.catalogs:
            for image in Content.images:
                if image['name'] != "ConfigServer":
                    app_name = "%s-%s" % \
                        (image['name'], catalog['cloud_parent'])
                    # 'while not' used to loop until image pushed
                    # FIXME: better way?
                    while not page.verify_image_push(catalog['name'], app_name, image):
                        time.sleep(30)
                    else:
                        page.launch_app(catalog['name'], app_name, image)

    def test_verify_launch(self, mozwebqa):
        '''
        verify app launch
        '''
        page = self.aeolus.load_page('Aeolus')
        page.login()

        for catalog in Content.catalogs:
            for image in Content.images:
                if image['name'] != "ConfigServer":
                    app_name = "%s-%s" % \
                        (image['name'], catalog['cloud_parent'])
                    # 'while not' used to loop until image pushed
                    # FIXME: better way?
                    while not page.verify_launch(app_name):
                        time.sleep(10)
                    else:
                        print "App '%s' launched" % app_name


    ###
    # TOD: 
    # api function for reference
    # use/extend for polling status
    ###
    @pytest.mark.skipif("1 == 1")
    def test_poll_images(self, mozwebqa):
        '''
        poll image build and return status
        '''
        print "### Images ###"
        images = self.api.get_element_id_list("images", "image")
        for image_id in images:
            image_detail = self.api.get_detailed_info("images", image_id)
            print "%s (%s)" % (image_detail['name'], image_id)

        # return XML more complex, not verified
        print "### Target Images ###"
        target_images = self.api.get_element_id_list("target_images", "target_image")
        for target_image_id in target_images:
            target_image_detail = self.api.get_detailed_info("target_images", target_image_id)
            print "%s (%s)" % (target_image_detail['template'], target_image_id)
