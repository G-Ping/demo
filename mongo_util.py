#!/usr/bin/python
# -*- coding: gb2312 -*-
#-*-coding=utf-8
import pymongo
import sys

def get_con(host='localhost'):
    con = pymongo.MongoClient( host, 27017 )
    return con

def find_one(muser=get_con().mydb.user):
    return muser.find_one( )

def find(dict="{'id':1}",muser=get_con().mydb.user):
    return muser.find(eval(dict))

def dump(obj, nested_level=0, output=sys.stdout):
    spacing = '   '
    if type(obj) == dict:
        print >> output, '%s{' % ((nested_level) * spacing)
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print >> output, '%s%s:' % ((nested_level + 1) * spacing, k)
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s: %s' % ((nested_level + 1) * spacing, k, v)
        print >> output, '%s}' % (nested_level * spacing)
    elif type(obj) == list:
        print >> output, '%s[' % ((nested_level) * spacing)
        for v in obj:
            if hasattr(v, '__iter__'):
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s' % ((nested_level + 1) * spacing, v)
        print >> output, '%s]' % ((nested_level) * spacing)
    else:
        print >> output, '%s%s' % (nested_level * spacing, obj)

def dump1(cursor):
    if(isinstance(cursor,dict)):
        dump(cursor)
    else:
        for rs in cursor:
            dump(rs)
            
if __name__ == '__main__':
    dump1(find_one())
    dump1(find())
    
    #muser = get_con().mydb.user
    #dump1(muser.find_one()) # find a record
    #dump1(muser.find({'id':1})) # find a record by query
    #print muser.find({'id':1}).count()# get records number
    #dump1(muser.find({'id':1}).limit(3).skip(0)) # start index is 2 limit 3 records

    #mydb.add_user('test', 'test') # add a user
    #mydb.authenticate('test', 'test') # check auth
    #muser.create_index('id')
    #dump.dump1(muser.find().sort('id', pymongo.ASCENDING))# DESCENDING
    #con.drop_database(mydb)
    #muser.drop() delete table

    #muser.save({'id':1, 'name':{'gj':'df','sd':{'gj':'df','sd':'df'}}}) # add a record
    #muser.insert({'id':1, 'name':'hello'}) # add a record
    #muser.remove({'id':1}) # delet records where id = 1
    #muser.update({'id':1}, {'$set':{'name':'haha'}}) # update one recor