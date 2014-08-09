from flask import render_template, session
import pymysql
from web import app

__author__ = 'xu'


@app.route('/')
def index():
    param = {
        'blog_list': get_blog_list()
    }
    if len(param['blog_list']) > 1:
        param['blog'] = get_blog_by_id(param['blog_list'][0]['ID'])
    return render_template('index.html', **param)


def get_blog_list():
    conn = pymysql.connect(host='121.40.88.181', user='root', passwd='bronze', database='opticaline',
                           cursorclass=pymysql.cursors.DictCursor, charset="utf8")
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT ID, USER_ID, TITLE, CREATE_DATE, EDIT_DATE, TAG_ID FROM BLOG ORDER BY CREATE_DATE DESC''')
    blog = cursor.fetchall()
    cursor.close()
    conn.close()
    return blog


def get_blog_by_id(blog_id):
    conn = pymysql.connect(host='121.40.88.181', user='root', passwd='bronze', database='opticaline',
                           cursorclass=pymysql.cursors.DictCursor, charset="utf8")
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT ID, USER_ID, TITLE, CONTENT, CREATE_DATE, EDIT_DATE, TAG_ID FROM BLOG WHERE ID = %s''', [blog_id])
    blog = cursor.fetchone()
    cursor.close()
    conn.close()
    return blog
