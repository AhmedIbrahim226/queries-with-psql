import psycopg2
from psycopg2 import Error
from decouple import config

class DataBase:
    def connect(self):
        connection = psycopg2.connect(
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            host='localhost',
            port='5432',
            dbname='postgres'
        )
        connection.autocommit = True
        return connection.cursor()

    def getAllDatabase(self):
        cursor = self.connect()
        try:
            cursor.execute(''' select datname from pg_database; ''')
            for select in cursor.fetchall():
                for item in select:
                    print(item)
            cursor.connection.commit()
            cursor.connection.close()
        except (Exception, Error) as e:
            print(e)

    def createDatabase(self, databasename):
        cursor = self.connect()
        try:
            cursor.execute(f''' create database {databasename}; ''')
            print('Created Successfully')
            cursor.connection.commit()
            cursor.connection.close()
        except (Exception, Error) as e:
            print(e)

    def removeDatabase(self, databasename):
        cursor = self.connect()
        try:
            cursor.execute(f''' drop database {databasename}; ''')
            print(f'The database with name {databasename} deleted.')
            cursor.connection.commit()
            cursor.connection.close()
        except (Exception, Error) as error:
            print(error)

    def searchInDatabase(self, myWord):
        cursor = self.connect()
        try:
            cursor.execute(''' CREATE OR REPLACE FUNCTION global_search(
                                            search_term text,
                                            param_tables text[] default '{}',
                                            param_schemas text[] default '{public}',
                                            progress text default null -- 'tables','hits','all'
                                        )
                                        RETURNS table(schemaname text, tablename text, columnname text, rowctid tid)
                                        AS $$
                                        declare
                                          query text;
                                          hit boolean;
                                        begin
                                          FOR schemaname,tablename IN
                                              SELECT t.table_schema, t.table_name
                                              FROM   information_schema.tables t
                                            JOIN information_schema.table_privileges p ON
                                              (t.table_name=p.table_name AND t.table_schema=p.table_schema
                                                  AND p.privilege_type='SELECT')
                                            JOIN information_schema.schemata s ON
                                              (s.schema_name=t.table_schema)
                                              WHERE (t.table_name=ANY(param_tables) OR param_tables='{}')
                                                AND t.table_schema=ANY(param_schemas)
                                                AND t.table_type='BASE TABLE'
                                          LOOP
                                            IF (progress in ('tables','all')) THEN
                                              raise info '%', format('Searching globally in table: %I.%I',
                                                 schemaname, tablename);
                                            END IF;

                                            query := format('SELECT ctid FROM %I.%I AS t WHERE strpos(cast(t.* as text), %L) > 0',
                                                schemaname,
                                                tablename,
                                                search_term);
                                            FOR rowctid IN EXECUTE query
                                            LOOP
                                              FOR columnname IN
                                              SELECT column_name
                                              FROM information_schema.columns
                                              WHERE table_name=tablename
                                                AND table_schema=schemaname
                                              LOOP
                                            query := format('SELECT true FROM %I.%I WHERE cast(%I as text)=%L AND ctid=%L',
                                              schemaname, tablename, columnname, search_term, rowctid);
                                                EXECUTE query INTO hit;
                                            IF hit THEN
                                              IF (progress in ('hits', 'all')) THEN
                                                raise info '%', format('Found in %I.%I.%I at ctid %s',
                                                   schemaname, tablename, columnname, rowctid);
                                              END IF;
                                              RETURN NEXT;
                                            END IF;
                                              END LOOP; -- for columnname
                                            END LOOP; -- for rowctid
                                          END LOOP; -- for table
                                        END;
                                        $$ language plpgsql; ''')
            dsn = cursor.connection.dsn
            var = dsn.split()[2]
            var2 = var.split('=')

            cursor.execute(''' select datname from pg_database; ''')
            listDatabase = []
            for select in cursor.fetchall():
                for dbname in select:
                    listDatabase.append(dbname)

            cursor.execute(' SELECT table_name FROM information_schema.tables; ')
            listTables = []
            for alltb in cursor.fetchall():
                for alltb2 in alltb:
                    listTables.append(alltb2)

            if myWord in listDatabase:
                print(f'{myWord} is Database.')
            else:
                print(f"{myWord} isn't database")

            if myWord in listTables:
                print(rf"{myWord} it's in Database called: {var2[1]} and Table called: {myWord}.")
            else:
                print(f"{myWord} isn't table")

            cursor.execute(f''' select tablename, columnname from global_search('{myWord}'); ''')
            listWord = []
            for select in cursor.fetchall():
                for word in select:
                    listWord.append(word)

            if listWord:
                tabname = 0
                colname = 1
                while tabname < len(listWord):
                    print(
                        rf"{myWord} it's in Database called: {var2[1]} and in Table called: {listWord[tabname]} and in Column called: {listWord[colname]}")
                    tabname += 2
                    colname += 2
            else:
                print(f"{myWord} not found in columns")

        except (Exception, Error) as error:
            print(error)


obj = DataBase()



