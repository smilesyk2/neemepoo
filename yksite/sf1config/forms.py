# -*- coding: utf-8 -*-
from django import forms
from django.forms.formsets import formset_factory
from lib.sf1_python import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sf1_yesno_type = SF1_YESNO_TYPE()
sf1_source_type = SF1_SOURCE_TYPE()
sf1_subquery_type = SF1_SUBQUERY_TYPE()
sf1_date_dbformat = SF1_DATE_DBFORMAT()
sf1_dsn_type = SF1_DSN_TYPE()

L_SF1_YESNO_TYPE = []
L_SF1_YESNO_TYPE.extend(sf1_yesno_type.get_all_values())
L_SF1_SOURCE_TYPE = []
L_SF1_SOURCE_TYPE.extend(sf1_source_type.get_all_source_type())
L_SF1_SUBQUERY_TYPE = []
L_SF1_SUBQUERY_TYPE.extend(sf1_subquery_type.get_all_subquery_type())
L_SF1_DATE_DBFORMAT = []
L_SF1_DATE_DBFORMAT.extend(sf1_date_dbformat.get_all_date_dbformat())
L_SF1_DSN_TYPE = []
L_SF1_DSN_TYPE.extend(sf1_dsn_type.get_all_dsn_type())

SOURCE_TYPE = tuple(L_SF1_SOURCE_TYPE)
SOURCE_DATE_DBFORMAT = tuple(L_SF1_DATE_DBFORMAT)
SOURCE_DSN_TYPE = tuple(L_SF1_DSN_TYPE)
SOURCE_SUBQUERY_TYPE = tuple(L_SF1_SUBQUERY_TYPE)
SOURCE_SUBQUERY_STATEMENT = tuple(L_SF1_YESNO_TYPE)
SOURCE_CATALOG_HTMLPARSE = tuple(L_SF1_YESNO_TYPE)

print SOURCE_TYPE
print SOURCE_DATE_DBFORMAT
print SOURCE_DSN_TYPE
print SOURCE_SUBQUERY_TYPE
print SOURCE_SUBQUERY_STATEMENT
print SOURCE_CATALOG_HTMLPARSE

class SourceMetainfoForm(forms.Form):
    source_id = forms.CharField(max_length=30)
    source_type = forms.ChoiceField(widget=forms.Select, choices=SOURCE_TYPE)
    refcoll = forms.CharField(max_length=30) # 향후에 isc에 등록된 collection 목록을 보여주는 걸로 수정
    date_dbformat = forms.ChoiceField(widget=forms.Select, choices=SOURCE_DATE_DBFORMAT)
    date_order = forms.IntegerField()
    dsn_type = forms.ChoiceField(widget=forms.CheckboxInput, choices=SOURCE_DSN_TYPE)
    dsn_dsn = forms.CharField(max_length=30)
    primarykey = forms.CharField(max_length=30)
    
class SourceCatalogInfoForm(forms.Form):
    mapping_colnum = forms.IntegerField()
    mapping_tagname = forms.CharField(max_length=50)
    mapping_html = forms.ChoiceField(widget=forms.RadioSelect, choices=SOURCE_CATALOG_HTMLPARSE)
    
class SourceSubqueryForm(forms.Form):
    sub_order = forms.IntegerField()
    sub_type = forms.ChoiceField(widget=forms.Select, choices=SOURCE_SUBQUERY_TYPE)
    sub_separator = forms.CharField(max_length=10, required=False)
    sub_wherecnt = forms.IntegerField(required=False)
    sub_classname = forms.CharField(max_length=100, required=False)
    sub_usecnt = forms.IntegerField(required=False)
    sub_sql_statement = forms.ChoiceField(widget=forms.RadioSelect, choices=SOURCE_SUBQUERY_STATEMENT)
    sub_sql = forms.CharField(widget=forms.Textarea(attrs={'rows' : 4}))
    
SOURCE_FORM = [
               ('metainfo', SourceMetainfoForm),
               ('cataloginfo', SourceCatalogInfoForm),
               ('subquery', formset_factory(SourceSubqueryForm))
               ]

SOURCE_TEMPLATES = {
                    'metainfo' : "sf1config/source/metaInfo.html",
                    'catalogInfo' : "sf1config/source/catalogInfo.html",
                    'subQuery' : "sf1config/source/subQuery.html"
                    }
    