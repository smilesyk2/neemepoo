# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SF1_YESNO_TYPE():
    yes = ('y', 'yes')
    no = ('n', 'no')
    
    all_types = [ yes, no ]
    
    def get_all_values(self): return [ x for x in self.all_types ]
    
class SF1_SOURCE_TYPE():
    # 변수명 = ( '실제 config에 입력될 값', '화면에 표시될 이름')
    db     = ('db', 'DB')
    web    = ('web', 'Web')
    file   = ('file', 'File')
    
    all_types = [ db, web, file ]
    
    def get_all_source_type(self): return [ x for x in self.all_types ]
    
    
class SF1_SUBQUERY_TYPE():
    subquery = ('subQuery', 'subQuery')
    requery  = ('reQuery', 'reQuery')
    connectby = ('connectBy', 'connectBy')
    append = ('append', 'append')
    
    all_types = [ subquery, requery, connectby, append ]
    
    def get_all_subquery_type(self): return [ x for x in self.all_types ]
     
class SF1_DATE_DBFORMAT():
    none = ('none', 'none')
    etc = ('etc', 'ETC')
    
    all_types = [ none, etc ]
    
    def get_all_date_dbformat(self): return [ x for x in self.all_types ]
    
class SF1_DSN_TYPE():
    target = ('target', 'target')
    log    = ('log', 'log')
    
    all_types = [ target, log ]
    
    def get_all_dsn_type(self): return [ x for x in self.all_types ]