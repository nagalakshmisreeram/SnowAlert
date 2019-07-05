from azure.mgmt.subscription import SubscriptionClient
from azure.common.credentials import ServicePrincipalCredentials

{'id': '/subscriptions/0e2a4dad-3adf-49eb-bd3d-f606a97f8a16', 'subscription_id': '0e2a4dad-3adf-49eb-bd3d-f606a97f8a16', 'display_name': 'azpreprod - customer FDN', 'state': 'Enabled', 'subscription_policies': {'location_placement_id': 'Public_2014-09-01', 'quota_id': 'EnterpriseAgreement_2014-09-01', 'spending_limit': 'Off'}, 'authorization_source': 'RoleBased'}

CONNECTION_OPTIONS = [
    {
        'type': 'str',
        'name': 'username',
        'title': "Service Principal Username",
        'prompt': "The service principal username which can list your subscriptions",
        'placeholder': "sample-username",
        'required': True
    },
    {
        'type': 'str',
        'name': 'password',
        'title': "Password",
        'prompt': "Password for the Service Principal",
        'secret': True,
        'placeholder': "sample_password",
        'required': True
    },
    {
        'type': 'str',
        'name': 'tenant',
        'title': "Tenant ID",
        'prompt': "The Tenant ID for your Azure account",
        'default': 'sample-tenant',
        'required': True
    },
]

LANDING_TABLE_COLUMNS = [
    ('RAW', 'VARIANT'),
    ('EVENT_TIME', 'TIMESTAMP_LTZ'),
    ('ID', 'VARCHAR(1024)'),
    ('SUBSCRIPTION_ID', 'VARCHAR(1024)'),
    ('DISPLAY_NAME', 'VARCHAR(1024)'),
    ('STATE', 'VARCHAR(1024)'),
    ('SUBSCRIPTION_POLICIES', 'VARIANT'),
    ('AUTHORIZATION_SOURCE', 'VARCHAR(1024)'),
]


def connect(connection_name, options):
