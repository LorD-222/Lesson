from pywinservicemanager.WindowsServiceConfigurationManager import ServiceExists

serviceName = 'TestService'
serviceExists = ServiceExists(serviceName)
print serviceExists