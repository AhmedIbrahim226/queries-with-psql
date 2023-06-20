import psycopg2
from psycopg2 import Error
import requests


class JsonUrl:
    def __init__(self):

        try:
            connection = psycopg2.connect(user='ahmed', port='5432', host='localhost', password='123456789')
            connection.autocommit = True

            cursor = connection.cursor()
            cursor.execute(''' create database json; ''')
        except (Exception, Error):
            pass

        self.stats()
        self.pages_http_visa_com_ai()
        self.pages_http_visa_com_ai_headers()
        self.pages_http_visa_com_ai_tags()
        self.pages_http_visa_com_ai_2082()
        self.pages_http_visa_com_ai_2082_headers()
        self.pages_http_visa_com_ai_2082_tags()
        self.pages_http_visa_com_ai_2095()
        self.pages_http_visa_com_ai_2095_headers()
        self.pages_http_visa_com_ai_2095_tags()
        self.pages_http_visa_com_ai_8080()
        self.pages_http_visa_com_ai_8080_headers()
        self.pages_http_visa_com_ai_8080_tags()
        self.pages_http_visa_com_ai_8880()
        self.pages_http_visa_com_ai_8880_headers()
        self.pages_http_visa_com_ai_8880_tags()
        self.pages_http_www_visa_com_ai()
        self.pages_http_www_visa_com_ai_headers()
        self.pages_http_www_visa_com_ai_tags()
        self.pages_http_www_visa_com_ai_2082()
        self.pages_http_www_visa_com_ai_2082_headers()
        self.pages_http_www_visa_com_ai_2082_tags()
        self.pages_http_www_visa_com_ai_2095()
        self.pages_http_www_visa_com_ai_2095_headers()
        self.pages_http_www_visa_com_ai_2095_tags()
        self.pages_http_www_visa_com_ai_8080()
        self.pages_http_www_visa_com_ai_8080_headers()
        self.pages_http_www_visa_com_ai_8080_tags()
        self.pages_http_www_visa_com_ai_8880()
        self.pages_http_www_visa_com_ai_8880_headers()
        self.pages_http_www_visa_com_ai_8880_tags()
        self.pages_https_visa_com_ai()
        self.pages_https_visa_com_ai_headers()
        self.pages_https_visa_com_ai_tags()
        self.pages_https_visa_com_ai_2087()
        self.pages_https_visa_com_ai_2087_headers()
        self.pages_https_visa_com_ai_2087_tags()
        self.pages_https_visa_com_ai_2096()
        self.pages_https_visa_com_ai_2096_headers()
        self.pages_https_visa_com_ai_2096_tags()
        self.pages_https_visa_com_ai_8443()
        self.pages_https_visa_com_ai_8443_headers()
        self.pages_https_visa_com_ai_8443_tags()
        self.pages_https_www_visa_com_ai()
        self.pages_https_www_visa_com_ai_headers()
        self.pages_https_www_visa_com_ai_tags()
        self.pageSimilarityClusters()
        print('Successfully Imported')

    def connect(self):
        connection = psycopg2.connect(
            user='ahmed',
            password='123456789',
            host='localhost',
            port='5432',
            dbname='json'
        )
        connection.autocommit = True
        return connection.cursor()

    def request(self):
        req = requests.get('https://79y8g.csb.app/test.json').json()
        return req

    def stats(self):
        cursor = self.connect()
        req = self.request()
        stats = req['stats']
        statsKey = stats.keys()
        statsValue = stats.values()

        listStatsKey = []
        listStatsValue = []
        for key, value in zip(statsKey, statsValue):
            listStatsKey.append(key)
            listStatsValue.append(value)

        try:
            cursor.execute(f''' create table stats(
                                {listStatsKey[0]} varchar(200), {listStatsKey[1]} varchar(200), {listStatsKey[2]} varchar(200),
                                {listStatsKey[3]} varchar(200), {listStatsKey[4]} varchar(200), {listStatsKey[5]} varchar(200),
                                {listStatsKey[6]} varchar(200), {listStatsKey[7]} varchar(200), {listStatsKey[8]} varchar(200),
                                {listStatsKey[9]} varchar(200), {listStatsKey[10]} varchar(200), {listStatsKey[11]} varchar(200)
                                ); ''')
        except (Exception, Error):
            pass

        cursor.execute(f''' insert into stats (
        {listStatsKey[0]}, {listStatsKey[1]}, {listStatsKey[2]}, {listStatsKey[3]}, {listStatsKey[4]}, {listStatsKey[5]}, {listStatsKey[6]}, {listStatsKey[7]},
        {listStatsKey[8]}, {listStatsKey[9]}, {listStatsKey[10]}, {listStatsKey[11]}
          )values ( '{listStatsValue[0]}', '{listStatsValue[1]}', '{listStatsValue[2]}', '{listStatsValue[3]}',
                    '{listStatsValue[4]}', '{listStatsValue[5]}', '{listStatsValue[6]}', '{listStatsValue[7]}',
                    '{listStatsValue[8]}', '{listStatsValue[9]}', '{listStatsValue[10]}', '{listStatsValue[11]}') ''')

    def pages_http_visa_com_ai(self):
        cursor = self.connect()
        req = self.request()
        pages = req['pages']['http://visa.com.ai/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()
        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(rf''' create table pages_http_visa_com_ai(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); ''')
        except (Exception, Error):
            pass
        cursor.execute(rf''' insert into pages_http_visa_com_ai(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); ''')

    def pages_http_visa_com_ai_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://visa.com.ai/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))
        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(rf''' create table pages_http_visa_com_ai_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); ''')
        except (Exception, Error):
            pass
        for num in range(len(headers)):
            cursor.execute(fr''' insert into pages_http_visa_com_ai_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); ''')

    def pages_http_visa_com_ai_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://visa.com.ai/']['tags']
        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for inCol in listKeys[0]:
            listColumn.append(inCol)
        try:
            cursor.execute(rf''' create table pages_http_visa_com_ai_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); ''')
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(rf''' insert into pages_http_visa_com_ai_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); ''')

    def pages_http_visa_com_ai_2082(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['http://visa.com.ai:2082/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_2082(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_http_visa_com_ai_2082(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_http_visa_com_ai_2082_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://visa.com.ai:2082/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_2082_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_http_visa_com_ai_2082_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_visa_com_ai_2082_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://visa.com.ai:2082/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_2082_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_http_visa_com_ai_2082_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_visa_com_ai_2095(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['http://visa.com.ai:2095/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_2095(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_http_visa_com_ai_2095(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_http_visa_com_ai_2095_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://visa.com.ai:2095/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_2095_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_http_visa_com_ai_2095_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_visa_com_ai_2095_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://visa.com.ai:2095/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_2095_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_http_visa_com_ai_2095_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_visa_com_ai_8080(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['http://visa.com.ai:8080/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_8080(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_http_visa_com_ai_8080(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_http_visa_com_ai_8080_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://visa.com.ai:8080/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_8080_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_http_visa_com_ai_8080_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_visa_com_ai_8080_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://visa.com.ai:8080/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_8080_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_http_visa_com_ai_8080_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_visa_com_ai_8880(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['http://visa.com.ai:8880/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_8880(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_http_visa_com_ai_8880(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_http_visa_com_ai_8880_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://visa.com.ai:8880/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_8880_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_http_visa_com_ai_8880_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_visa_com_ai_8880_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://visa.com.ai:8880/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_http_visa_com_ai_8880_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_http_visa_com_ai_8880_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_www_visa_com_ai(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['http://www.visa.com.ai/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_http_www_visa_com_ai(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_http_www_visa_com_ai_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://www.visa.com.ai/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_http_www_visa_com_ai_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_www_visa_com_ai_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://www.visa.com.ai/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_http_www_visa_com_ai_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_www_visa_com_ai_2082(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['http://www.visa.com.ai:2082/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_2082(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_http_www_visa_com_ai_2082(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_http_www_visa_com_ai_2082_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://www.visa.com.ai:2082/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_2082_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_http_www_visa_com_ai_2082_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_www_visa_com_ai_2082_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://www.visa.com.ai:2082/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_2082_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_http_www_visa_com_ai_2082_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_www_visa_com_ai_2095(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['http://www.visa.com.ai:2095/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_2095(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_http_www_visa_com_ai_2095(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_http_www_visa_com_ai_2095_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://www.visa.com.ai:2095/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_2095_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_http_www_visa_com_ai_2095_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_www_visa_com_ai_2095_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://www.visa.com.ai:2095/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_2095_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_http_www_visa_com_ai_2095_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_www_visa_com_ai_8080(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['http://www.visa.com.ai:8080/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_8080(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_http_www_visa_com_ai_8080(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_http_www_visa_com_ai_8080_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://www.visa.com.ai:8080/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(rf''' create table pages_http_www_visa_com_ai_8080_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
                           )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(fr''' insert into pages_http_www_visa_com_ai_8080_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
                           )

    def pages_http_www_visa_com_ai_8080_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://www.visa.com.ai:8080/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(rf''' create table pages_http_www_visa_com_ai_8080_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
                           )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(rf''' insert into pages_http_www_visa_com_ai_8080_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
                           )

    def pages_http_www_visa_com_ai_8880(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['http://www.visa.com.ai:8880/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_8880(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_http_www_visa_com_ai_8880(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_http_www_visa_com_ai_8880_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['http://www.visa.com.ai:8880/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_8880_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_http_www_visa_com_ai_8880_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_http_www_visa_com_ai_8880_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['http://www.visa.com.ai:8880/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_http_www_visa_com_ai_8880_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_http_www_visa_com_ai_8880_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_visa_com_ai(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['https://visa.com.ai/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_https_visa_com_ai(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_https_visa_com_ai_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['https://visa.com.ai/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_https_visa_com_ai_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_visa_com_ai_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['https://visa.com.ai/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_https_visa_com_ai_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_visa_com_ai_2087(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['https://visa.com.ai:2087/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_2087(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_https_visa_com_ai_2087(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_https_visa_com_ai_2087_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['https://visa.com.ai:2087/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_2087_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_https_visa_com_ai_2087_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_visa_com_ai_2087_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['https://visa.com.ai:2087/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_2087_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_https_visa_com_ai_2087_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_visa_com_ai_2096(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['https://visa.com.ai:2096/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_2096(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_https_visa_com_ai_2096(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_https_visa_com_ai_2096_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['https://visa.com.ai:2096/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_2096_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_https_visa_com_ai_2096_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_visa_com_ai_2096_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['https://visa.com.ai:2096/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_2096_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_https_visa_com_ai_2096_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_visa_com_ai_8443(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['https://visa.com.ai:8443/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_8443(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_https_visa_com_ai_8443(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_https_visa_com_ai_8443_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['https://visa.com.ai:8443/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_8443_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_https_visa_com_ai_8443_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_visa_com_ai_8443_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['https://visa.com.ai:8443/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_https_visa_com_ai_8443_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(
                rf''' insert into pages_https_visa_com_ai_8443_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_www_visa_com_ai(self):
        cursor = self.connect()

        req = self.request()
        pages = req['pages']['https://www.visa.com.ai/']
        del pages['headers']
        del pages['tags']
        pagesKey = pages.keys()
        pagesValue = pages.values()

        listPagesKey = []
        listPagesValue = []
        for key, value in zip(pagesKey, pagesValue):
            listPagesKey.append(key)
            listPagesValue.append(value)
        try:
            cursor.execute(
                rf''' create table pages_https_www_visa_com_ai(
                                                    {listPagesKey[0]} varchar(200), {listPagesKey[1]} varchar(200), {listPagesKey[2]} varchar(200),
                                                    {listPagesKey[3]} varchar(200), {listPagesKey[4]} varchar(200), {listPagesKey[5]} varchar(200),
                                                    {listPagesKey[6]} varchar(200), {listPagesKey[7]} varchar(200), {listPagesKey[8]} varchar(200),
                                                    {listPagesKey[9]} varchar(200), {listPagesKey[10]} varchar(200)
                                                    ); '''
            )
        except (Exception, Error):
            pass

        cursor.execute(
            rf''' insert into pages_https_www_visa_com_ai(
                                                {listPagesKey[0]}, {listPagesKey[1]}, {listPagesKey[2]},
                                                {listPagesKey[3]}, {listPagesKey[4]}, {listPagesKey[5]},
                                                {listPagesKey[6]}, {listPagesKey[7]}, {listPagesKey[8]},
                                                {listPagesKey[9]}, {listPagesKey[10]}
                                                ) values (
                                                    '{listPagesValue[0]}', '{listPagesValue[1]}', '{listPagesValue[2]}', {listPagesValue[3][0], listPagesValue[3][1]},
                                                    '{listPagesValue[4]}', '{listPagesValue[5]}', '{listPagesValue[6]}', '{listPagesValue[7]}',
                                                    '{listPagesValue[8]}', '{listPagesValue[9]}', '{listPagesValue[10]}'
                                                ); '''
        )

    def pages_https_www_visa_com_ai_headers(self):
        cursor = self.connect()
        req = self.request()

        headers = req['pages']['https://www.visa.com.ai/']['headers']

        listKeys = []
        for num in range(len(headers)):
            listKeys.append(list(headers[num].keys()))

        listColumn = []
        for i in listKeys[0]:
            listColumn.append(i)
        try:
            cursor.execute(
                rf''' create table pages_https_www_visa_com_ai_headers(
                                id bigserial primary key,
                                {listColumn[0]} varchar(500),
                                {listColumn[1]} varchar(500),
                                {listColumn[2]} varchar(500),
                                {listColumn[3]} varchar(500) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(headers)):
            cursor.execute(
                fr''' insert into pages_https_www_visa_com_ai_headers(
                                                                        {list(headers[num].keys())[0]},
                                                                        {list(headers[num].keys())[1]},
                                                                        {list(headers[num].keys())[2]},
                                                                        {list(headers[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(headers[num].values())[0]}',
                                                                        '{list(headers[num].values())[1]}',
                                                                        '{list(headers[num].values())[2]}',
                                                                        '{list(headers[num].values())[3]}'
                                                                        ); '''
            )

    def pages_https_www_visa_com_ai_tags(self):
        cursor = self.connect()
        req = self.request()

        tags = req['pages']['https://www.visa.com.ai/']['tags']

        listKeys = []
        for num in range(len(tags)):
            listKeys.append(list(tags[num].keys()))

        listColumn = []
        for iTag in listKeys[0]:
            listColumn.append(iTag)
        try:
            cursor.execute(
                rf''' create table pages_https_www_visa_com_ai_tags(
                                id bigserial primary key,
                                {listColumn[0]} varchar(200),
                                {listColumn[1]} varchar(200),
                                {listColumn[2]} varchar(200),
                                {listColumn[3]} varchar(200) ); '''
            )
        except (Exception, Error):
            pass

        for num in range(len(tags)):
            cursor.execute(rf''' insert into pages_https_www_visa_com_ai_tags(
                                                                        {list(tags[num].keys())[0]},
                                                                        {list(tags[num].keys())[1]},
                                                                        {list(tags[num].keys())[2]},
                                                                        {list(tags[num].keys())[3]}
                                                                        ) values (
                                                                        '{list(tags[num].values())[0]}',
                                                                        '{list(tags[num].values())[1]}',
                                                                        '{list(tags[num].values())[2]}',
                                                                        '{list(tags[num].values())[3]}'
                                                                        ); '''
                           )

    def pageSimilarityClusters(self):
        cursor = self.connect()
        req = self.request()

        pageSimilarity = req['pageSimilarityClusters']
        # columnName = list(pageSimilarity.keys())[0]
        columnName = '_39c12256_67dc_469c_a969_23b21e215f9c'

        try:
            cursor.execute(rf''' create table pageSimilarityClusters(
                                id bigserial primary key,
                                {columnName} varchar(200)
                                 ); '''
                           )
        except (Exception, Error):
            pass

        for val in pageSimilarity.values():
            for val2 in val:
                cursor.execute(f''' insert into pageSimilarityClusters ({columnName}) values ('{val2}') ; ''')
