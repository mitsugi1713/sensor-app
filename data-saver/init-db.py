import helper
session = helper.get_session()

print("\nCreating Keyspace")
session.execute(
    'CREATE KEYSPACE IF NOT EXISTS sensors WITH replication = {\'class\': \'NetworkTopologyStrategy\', \'datacenter\' : \'1\'  }'
)

print("\nCreating Table")
session.execute(
    'CREATE TABLE IF NOT EXISTS sensors.temperature (id timeuuid PRIMARY KEY, record_date date, record_time time, sensor textm temperature float)'
)