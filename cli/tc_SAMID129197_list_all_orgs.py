import sys, os, subprocess, commands, time
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129197_list_all_orgs(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#create an org
		orgname = ee.org1 + time.strftime('%Y%m%d%H%M%S')
		eu().sam_create_org(session, orgname)
	
		#list all orgs
                cmd="headpin -u admin -p admin org list"
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list organization: %s"%cmd)
                logging.info("result of list organization: %s"%str(ret))
                logging.info("output of list organization: %s"%str(output))

                if ret == 0 and orgname in output:
                        logging.info("It's successful to list all orgs.")
                else:
                        raise error.TestFail("Test Failed - Failed to list all orgs.")

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do list all orgs:"+str(e))
	finally:
		eu().sam_delete_org(session, orgname)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
