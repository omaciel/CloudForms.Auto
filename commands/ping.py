#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Ping:
    _command_ = "ping"
    _user_flag_ = "-u"
    _password_flag_ = "-p"
    
    def ping_error(self, u="admin", p="admin"):
        p = subprocess.Popen([self._command_, self._user_flag_, u, self._password_flag_, p], stdout=subprocess.PIPE)
        
        
        
        
