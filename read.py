import interface
import snap7
import time
tuo_area=(0x84,)#0x81:I区，0x82:Q区，0x83:M区，0x84:DB,V区
tuo_dbnumber=(0,)#DB号，若非DB即为0
tuo_start=(100,)#数据其实位置
tuo_size=(4,)#数据宽带


def ri():
      global link_1  
      global i,b
      i=0
      b=0
      if interface.dict_1['enable links']==True:
         link_1=snap7.client.Client()#与PLC建立连接
         #link_1.set_connection_type(3)
         link_1.connect(interface.dict_1['Ipaddress'],rack=0,slot=1)
         interface.dict_1['link_signal']=link_1.get_connected()
         interface.dict_1['db_cycle-sum']=int((interface.dict_1['db_end']-interface.dict_1['db_start']+1)/4)
         interface.dict_1['db_byte-sum']=(interface.dict_1['db_end']-interface.dict_1['db_start']+1)
         print(interface.dict_1['link_signal'])
         
      if interface.dict_1['link_signal']==True  :
          interface.dict_1['enable links']=False
          DB_0=link_1.read_area(snap7.types.Areas.DB,1,interface.dict_1['db_start'], interface.dict_1['db_byte-sum'])
          while i<interface.dict_1['db_cycle-sum'] :
               interface.list1[i]=snap7.util.get_real(DB_0,b)
               interface.list1[i]=format(interface.list1[i],'0.2f')#保留小数点后4位
               print(interface.list1[i])
               i=i+1
               b=b+4               
