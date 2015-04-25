# Server Specific Configurations
server = {
    'port': '8081',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'joulupukki.api.controllers.root.RootController',
    'modules': ['joulupukki.api'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/joulupukki/templates',
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}

logging = {
#    'root': {'level': 'INFO', 'handlers': ['console']},
    'root': {'level': 'DEBUG', 'handlers': ['console']},
    'loggers': {
        'joulupukki': {'level': 'DEBUG', 'handlers': ['console']},
        'pecan.commands.serve': {'level': 'DEBUG', 'handlers': ['console']},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s] '
                       '%(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': ('%(asctime)s [%(padded_color_levelname)s] [%(name)s] '
                       '%(message)s'),
        '__force_dict__': True
        }
    }
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
workspace_path = '%(confdir)s/../output'
rabbit_server = "127.0.0.1"
rabbit_port = 5672
rabbit_db = "joulupukki"
mongo_server = "127.0.0.1"
mongo_port = 27017
mongo_db = "joulupukki"
github_id = "666ff51d51afc14ab79c"
github_secret = "67c5dc2cf8dbb94c4d002ce08a406b64697e7265"



# TODO DELETE ME!!!!
distros = (
           ("ubuntu_10.04", "ubuntu:10.04", "deb"),
           ("ubuntu_12.04", "ubuntu:12.04", "deb"),
           ("ubuntu_14.04", "ubuntu:14.04", "deb"),
           ("debian_7", "debian:7", "deb"),
           ("debian_8", "debian:8", "deb"),
           ("centos_6", "centos:6", "rpm"),
           ("centos_7", "centos:7", "rpm"),
        )

#
# All configurations are accessible at::
# pecan.conf
