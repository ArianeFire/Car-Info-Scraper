# coding: utf-8
from __future__ import unicode_literals
import MySQLdb;

def insertMarque(name, id):
    db = MySQLdb.connect(host = "127.0.0.1", port=3306, user = "root", passwd = "", db = "pfadb");
    cursor = db.cursor();
    cursor.execute("""INSERT INTO marques (nom, id) VALUES(%s, %s)""", (name,id,));
    db.commit();

def insertModele(name, id_marque, id):
    db = MySQLdb.connect(host = "127.0.0.1", port=3306, user = "root", passwd = "", db = "pfadb");
    cursor = db.cursor();
    cursor.execute("""INSERT INTO modeles (nom, id_marque, id) VALUES(%s, %s, %s,)""", (name, id_marque, id));
    db.commit();

def insertType(nom, id_modele):
    db = MySQLdb.connect(host = "127.0.0.1", port=3306, user = "root", passwd = "", db = "pfadb");
    cursor=db.cursor();
    cursor.execute("""INSERT INTO types (nom, id_modele) VALUES(%s, %s,)""", (nom, id_modele));
    db.commit();