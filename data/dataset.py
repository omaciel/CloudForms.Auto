# generated from generate_dataset.py
# based on list definitions in raw_data.py

class Admin(object):
    '''
    Define users and groups
    '''
    user_groups = [
        {"name" : "admin",
        "description" : "Global admins. With great power comes great responsibility",
        "permissions" : ['Global Administrator'] },
        {"name" : "cfmanagers",
        "description" : "Global admins. With great power comes great responsibility",
        "permissions" : ['Global Administrator'] },
        {"name" : "qe",
        "description" : "real QE users",
        "permissions" : [] },
        {"name" : "cfusers",
        "description" : "Limited privilege users",
        "permissions" : ['Global Cloud Resource Zone User'] },
        ]

    users = [
        {"fname" : "Auto",
        "lname" : "Roboto",
        "email" : "admin@redhat.com",
        "username" : "automation",
        "passwd" : "redhat",
        "max_instances" : "",
        "user_groups" : ['admin'],
        "permissions" : [] },
        {"fname" : "Aaron",
        "lname" : "Weitekamp",
        "email" : "aweiteka@redhat.com",
        "username" : "aweiteka-admin",
        "passwd" : "redhat",
        "max_instances" : "20",
        "user_groups" : ['qe','cfmanagers'],
        "permissions" : ['Global Administrator'] },
        {"fname" : "Aaron",
        "lname" : "Weitekamp",
        "email" : "aweiteka@redhat.com",
        "username" : "aweiteka-user",
        "passwd" : "redhat",
        "max_instances" : "20",
        "user_groups" : ['cfusers'],
        "permissions" : [] },
        {"fname" : "Joe",
        "lname" : "User",
        "email" : "juser@example.com",
        "username" : "juser",
        "passwd" : "jpassword",
        "max_instances" : "20",
        "user_groups" : ['qe','cfmanagers'],
        "permissions" : [] },
        {"fname" : "James",
        "lname" : "Laska",
        "email" : "jlaska@redhat.com",
        "username" : "jlaska",
        "passwd" : "redhat",
        "max_instances" : "20",
        "user_groups" : ['qe','cfmanagers'],
        "permissions" : [] },
        {"fname" : "Milan",
        "lname" : "Falenik",
        "email" : "mfalesni@redhat.com",
        "username" : "mfalesni",
        "passwd" : "redhat",
        "max_instances" : "20",
        "user_groups" : ['qe','cfmanagers'],
        "permissions" : [] },
        {"fname" : "Gabriel",
        "lname" : "Szasz",
        "email" : "gszasz@redhat.com",
        "username" : "gszasz",
        "passwd" : "redhat",
        "max_instances" : "20",
        "user_groups" : ['qe','cfmanagers'],
        "permissions" : [] },
        ]

    selfservice_quota = "10"

class Provider(object):
    '''
    Define providers and provider accounts
    '''
    # provider_name string must match conductor
    # valid account types: "ec2", "rhevm", "vsphere"
    accounts = [

        {"type" : "rhevm",
        "provider_name" : "rhevm-30",
        "provider_account_name" : "rhevm-30",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "rhevm",
        "provider_name" : "rhevm-31",
        "provider_account_name" : "rhevm-31",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "vsphere",
        "provider_name" : "vsphere-4",
        "provider_account_name" : "vsphere-4",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "vsphere",
        "provider_name" : "vsphere-5",
        "provider_account_name" : "vsphere-5",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "ec2",
        "provider_name" : "ec2-ap-northeast-1",
        "provider_account_name" : "ec2-ap-northeast-1",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "ec2",
        "provider_name" : "ec2-ap-southeast-1",
        "provider_account_name" : "ec2-ap-southeast-1",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "ec2",
        "provider_name" : "ec2-ap-southeast-2",
        "provider_account_name" : "ec2-ap-southeast-2",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "ec2",
        "provider_name" : "ec2-eu-west-1",
        "provider_account_name" : "ec2-eu-west-1",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "ec2",
        "provider_name" : "ec2-sa-east-1",
        "provider_account_name" : "ec2-sa-east-1",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "ec2",
        "provider_name" : "ec2-us-east-1",
        "provider_account_name" : "ec2-us-east-1",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "ec2",
        "provider_name" : "ec2-us-west-1",
        "provider_account_name" : "ec2-us-west-1",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" },

        {"type" : "ec2",
        "provider_name" : "ec2-us-west-2",
        "provider_account_name" : "ec2-us-west-2",
        "provider_account_priority" : "",
        "provider_account_quota" : "32" }

        ]

    resource_profiles = [
        {"name" : "small-i386",
        "memory" : "512",
        "cpu_count" : "1",
        "storage" : "",
        "arch" : "i386"}
        ]

    # Create a cluster for each provider account name
    cloud_resource_clusters = [
            dict(name=a['provider_account_name'],
                 description='Cluster %s' % a['provider_account_name'],
                 provider=a['provider_name']) for a in accounts]

class Environment(object):
    '''
    Define environments and pools
    '''
    clouds = [
        {"name" : "Private",
        "max_running_instances" : "24",
        "enabled_provider_accounts" : \
            # All provider_account_name's where type is either rhevm or vsphere
            [a['provider_account_name'] for a in Provider.accounts if a['type'] in ['rhevm','vsphere']]
            },
        {"name" : "Public_EC2",
        "max_running_instances" : "24",
        "enabled_provider_accounts" : \
            # All provider_account_name's where type is ec2
            [a['provider_account_name'] for a in Provider.accounts if a['type'] in ['ec2']]
            }
        ]

    pools = [
        {"name" : "RHEV-30",
        "environment_parent" : clouds[0]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "RHEV-31",
        "environment_parent" : clouds[0]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "vSphere-4",
        "environment_parent" : clouds[0]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "vSphere-5",
        "environment_parent" : clouds[0]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "APAC-NE",
        "environment_parent" : clouds[1]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "APAC-SE-1",
        "environment_parent" : clouds[1]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "APAC-SE-2",
        "environment_parent" : clouds[1]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "EU",
        "environment_parent" : clouds[1]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "SouthAmerica",
        "environment_parent" : clouds[1]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "US-East",
        "environment_parent" : clouds[1]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "US-West1",
        "environment_parent" : clouds[1]['name'],
        "quota" : "10",
        "enabled" : True},
        {"name" : "US-West2",
        "environment_parent" : clouds[1]['name'],
        "quota" : "10",
        "enabled" : True}

        ]

class Content(object):
    '''
    Define catalogs, images and deployables
    '''
    # FIXME - this is easy to screw up, perhaps make it dynamically generated, like clusters
    catalogs = [
        {"name" : "Private apps-RHEV-30",
        "pool_parent" : Environment.pools[0]['name'],
        "cloud_parent" : "Private",
        "resource_cluster" : Provider.cloud_resource_clusters[0]['name']},
        {"name" : "Private apps-RHEV-31",
        "pool_parent" : Environment.pools[1]['name'],
        "cloud_parent" : "Private",
        "resource_cluster" : Provider.cloud_resource_clusters[1]['name']},
        {"name" : "Private apps-vSphere-4",
        "pool_parent" : Environment.pools[2]['name'],
        "cloud_parent" : "Private",
        "resource_cluster" : Provider.cloud_resource_clusters[2]['name']},
        {"name" : "Private apps-vSphere-5",
        "pool_parent" : Environment.pools[3]['name'],
        "cloud_parent" : "Private",
        "resource_cluster" : Provider.cloud_resource_clusters[3]['name']},
        {"name" : "Public apps-APNE",
        "pool_parent" : Environment.pools[4]['name'],
        "cloud_parent" : "Public_EC2",
        "resource_cluster" : Provider.cloud_resource_clusters[4]['name']},
        {"name" : "Public apps-APSE-1",
        "pool_parent" : Environment.pools[5]['name'],
        "cloud_parent" : "Public_EC2",
        "resource_cluster" : Provider.cloud_resource_clusters[5]['name']},
        {"name" : "Public apps-APSE-2",
        "pool_parent" : Environment.pools[6]['name'],
        "cloud_parent" : "Public_EC2",
        "resource_cluster" : Provider.cloud_resource_clusters[6]['name']},
        {"name" : "Public apps-EU",
        "pool_parent" : Environment.pools[7]['name'],
        "cloud_parent" : "Public_EC2",
        "resource_cluster" : Provider.cloud_resource_clusters[7]['name']},
        {"name" : "Public apps-SA",
        "pool_parent" : Environment.pools[8]['name'],
        "cloud_parent" : "Public_EC2",
        "resource_cluster" : Provider.cloud_resource_clusters[8]['name']},
        {"name" : "Public apps-US-East",
        "pool_parent" : Environment.pools[9]['name'],
        "cloud_parent" : "Public_EC2",
        "resource_cluster" : Provider.cloud_resource_clusters[9]['name']},
        {"name" : "Public apps-US-West1",
        "pool_parent" : Environment.pools[10]['name'],
        "cloud_parent" : "Public_EC2",
        "resource_cluster" : Provider.cloud_resource_clusters[10]['name']},
        {"name" : "Public apps-US-West2",
        "pool_parent" : Environment.pools[11]['name'],
        "cloud_parent" : "Public_EC2",
        "resource_cluster" : Provider.cloud_resource_clusters[11]['name']},
        ]

    configserver = {"name" : "ConfigServer",
        "template" : "rhel-x86_64-6Server-cf-configserver.xml",
        "version" : "0.4.12",
        "releasever" : "6Server",
        "basearch" : "x86_64",
        "profile" : "small-x86_64"}

