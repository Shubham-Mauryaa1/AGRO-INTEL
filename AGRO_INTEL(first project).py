import mysql.connector as c
from tabulate import tabulate
m=c.connect(host='localhost',passwd='admin123',user='root')
cu=m.cursor()
cu.execute('create database if not exists AGRO_INTEl')
cu.execute('use AGRO_INTEL')
cu.execute(""" create table if not exists crops(crop_id varchar(100),crop_name varchar(100),type varchar(100),ideal_climate varchar(120),
           idealtemp varchar(100),region varchar(100))""")
cu.execute("create table if not exists requirements(crop_id varchar(100),pH_level float(10),moisture_level float(10))")
cu.execute("create table if not exists irrigation_source(crop_id varchar(100),water_level int(10),sources varchar(100))")
cu.execute("create table if not exists pest_control(pest_type varchar(100),pest_control_method varchar(100),charges_per_bigha int(10))")
cu.execute("create table if not exists schemes(scheme_name varchar(100),government varchar(100),key_benefits varchar(200))")
cu.execute("""create table if not exists fertilizers(fertilizer_name varchar(100),type varchar(100),usage_per_bigha varchar(100),
           estm_price_per_50kg_bag int)""")
cu.execute("create table if not exists market(crop_id varchar(100),market_sales int,year int,total_qty_sold int)")
cu.execute("create table if not exists user_data(user_name varchar(100),password varchar(100))")
cu.execute("create table if not exists tool_usage(name varchar(100),usage1 varchar(100))")

cu.execute("SELECT COUNT(*) from crops")
if cu.fetchone()[0] == 0:
   cu.execute("""insert into crops values 
   ('WHT101', 'Wheat', 'Rabi', 'Cool-Dry', '10-25°C', 'Punjab'),
   ('MZ102', 'Maize', 'Kharif', 'Warm', '18-27°C', 'Uttar Pradesh'),
   ('RCE103', 'Rice', 'Kharif', 'Humid', '20-38°C', 'West Bengal'),
   ('JUT104', 'Jute', 'Kharif', 'Humid', '24-37°C', 'Assam'),
   ('GRD105', 'Groundnut', 'Kharif', 'Warm-Dry', '25-35°C', 'Gujarat'),
   ('COT106', 'Cotton', 'Kharif', 'Hot-Dry', '21-30°C', 'Maharashtra'),
   ('RGG107', 'Ragi', 'Kharif', 'Warm', '22-27°C', 'Karnataka'),
   ('COC108', 'Coconut', 'Perennial', 'Hot-Humid', '27-32°C', 'Kerala')""")
   m.commit()


cu.execute("SELECT COUNT(*) from fertilizers")
if cu.fetchone()[0]==0:
   cu.execute("""insert into fertilizers values
   ('urea', 'inorganic', '20-30 kg', 300),
   ('dap', 'inorganic', '15-25 kg', 450),
   ('mop', 'inorganic', '10-20 kg', 400),
   ('vermicompost', 'organic', '40-50 kg', 500),
   ('cow dung compost', 'organic', '50-60 kg', 200)""")
   m.commit()


cu.execute("SELECT COUNT(*) from irrigation_source")
if cu.fetchone()[0]==0:
   cu.execute("""INSERT INTO irrigation_source (crop_id, water_level, sources) VALUES
('WHT101', 800, 'Tube well'),
('MZ102', 700, 'Canal'),
('RCE103', 1500, 'Canal'),
('JUT104', 1400, 'Rain-fed'),
('GRD105', 600, 'Borewell'),
('COT106', 1200, 'Rain-fed'),
('RGG107', 500, 'Borewell'),
('COC108', 2500, 'Rainwater')
""")
m.commit()



cu.execute("SELECT COUNT(*) from pest_control")
if cu.fetchone()[0]==0:
   cu.execute("""
   INSERT INTO pest_control (pest_type, pest_control_method, charges_per_bigha) VALUES
   ('insecticide','Imidacloprid Spray',250),
   ('nematodes','Neem Cake Application',300),
   ('mites','Sulphur Dusting',200),
   ('aphids','Neem Oil Spray',150),
   ('locusts','Chlorpyrifos Spray',500)
   """)
   m.commit()


cu.execute("SELECT COUNT(*) from requirements")
if cu.fetchone()[0]==0:
   cu.execute("""
   INSERT INTO requirements (crop_id, pH_level, moisture_level) VALUES
   ('WHT101',6.5,20),
   ('RCE103',5.8,30),
   ('COT106',6.8,18),
   ('RGG107',5.5,22),
   ('COC108',6.0,28)
   """)
   m.commit()

cu.execute("SELECT COUNT(*) from market")
if cu.fetchone()[0]==0:
   cu.execute("""INSERT INTO market (crop_id, market_sales, year, total_qty_sold) VALUES
('WHT101', 500000, 2024, 1500),
('MZ102', 420000, 2024, 1300),
('RCE103', 720000, 2024, 1800),
('JUT104', 280000, 2023, 900),
('GRD105', 390000, 2024, 1100),
('COT106', 460000, 2023, 1200),
('RGG107', 210000, 2024, 900),
('COC108', 800000, 2023, 2500)""")
m.commit()


cu.execute("SELECT COUNT(*) from schemes")
if cu.fetchone()[0]==0:
   cu.execute("""
   INSERT INTO schemes (scheme_name, government, key_benefits) VALUES
   ('kisan samman nidhi', 'Central', '₹6000 yearly direct benefit to eligible farmers'),
   ('kalia yojana', 'State', 'Financial + insurance support for small/marginal farmers'),
   ('rythu bandhu', 'state', 'Investment support of ₹5000/acre per season in Telangana'),
   ('fasal bima yojana', 'Central', 'Crop insurance with low premium for Kharif/Rabi crops')
   """)
   m.commit()


cu.execute("SELECT COUNT(*) from tool_usage")
if cu.fetchone()[0]==0:
   cu.execute("""
   INSERT INTO tool_usage (name,usage1) VALUES
   ('tractor','ploughing,tilling'),
   ('power sprayer','Sprays pesticides/insecticides'),
   ('seed drill','Plants seeds at uniform depth and spacing'),
   ('weeder','Removes unwanted weeds')
   """)
   m.commit()





def login_page():
 while True:
    print("""
    1. Sign up (New user)
    2. Login as admin
    3. Login as farmer
    4. Exit
    """)
    r=int(input('Enter your choice: '))
    if r==1:
        sign_up()
    elif r==2:
        admin_page()
    elif r==3:
        farmer_page() 
    elif r==4:
        print("Thank You(:")
        break
def sign_up():
   print("""Enter New username and password""") 
   n=input("Input new username:")
   cu.execute("select user_name from user_data")
   d=cu.fetchall()
   l=[]
   for i in d:
      l.append(i[0])
   if n in l:   
      print("user name already existed!")
      n=input("Input another nusername:")
      p=input("Input password(Password must be strong):")
      cu.execute("insert into user_data values('{}','{}')".format(n, p)) 
      m.commit() 
      print("Registration Done Successfully!!\n")  
   else:
      p = input("Input password(Password must be strong):") 
      cu.execute("insert into user_data values('{}','{}')".format(n,p)) 
      m.commit() 
      print("Registration Done Successfully!!\n")   
def admin_page():
 password=input('Enter password: ')
 if password=='7749':

   while True:
      print("""
            1.delete user data
            2. update market data
            3.Go back to login page
            4.exit""")
      b =int(input("Enter your Choice:"))
      if b==1:
         cu.execute("select user_name from user_data") 
         z=cu.fetchall() 
         print(z)
         n=input("enter user name which has to be deleted:")
         p=input("you really want to delete this data? (yes/no):") 
         if p=="yes": 
           cu.execute("delete from user_data where user_name='{}'".format(n)) 
           m.commit() 
           print("SUCCESSFULLY DELETED!!") 
         else:
          print("NOT DELETED")
      elif b==2:
         cu.execute('select crop_name,crop_id from crops')
         h=cu.fetchall()
         k=[]
         for i in h:
          g=list(i)
          k.append(g)
         print(tabulate(k,headers=('crop_name','crop_id'),tablefmt="fancy_grid"))
         z=input("enter crop id for which data has to update")
         x=int(input("enter new market sales per year"))
         y=int(input("enter new total qty sold"))
         p=int(input("enter year of the data"))
         cu.execute("update market set market_sales={} where crop_id='{}'".format(x,z))
         cu.execute("update market set total_qty_sold={} where crop_id='{}'".format(y,z))
         cu.execute("update market set year={} where crop_id='{}'".format(p,z))
         m.commit()
         print("succefulyy updated")
      elif b==3:
         login_page()
def farmer_page():
   a=input("enter username-->")
   cu.execute("select user_name from user_data")
   c=cu.fetchall()
   l=[]
   for i in c:
      l.append(i[0])
   if a in l:
      b=input("enter the password-->")
      cu.execute("select password from user_data where user_name ='{}'".format(a))
      d=cu.fetchall()
      o=[]
      for i in d:
        o.append(i[0])
      if b in o:
         print("succesfully login:)")
         search_page()
      elif b not in o:
         print('wrong password! re-enter your password:->')
         v=input('re-enter your password :')
         if v in o:
            print('successfully login')
            search_page()
         else:
            print('too many attempts! create new account --->')
            cu.execute("delete from user_data where user_name='{}'".format(a)) 
            m.commit()
            sign_up()
   else:
      print('username not found!')
      login_page()  
      print('create new username through sign up')    
def search_page():
   while True:
      print("""
1.crop information
2.fertilizer suggestion
3.pest control info
4.irrigation info
5.market trends
6.tool usage guide
7.government schemes
8.back to login page
""")
      x=int(input('enter your choice:'))
      if x==1:
         cu.execute('select crop_name,crop_id from crops')
         h=cu.fetchall()
         k=[]
         for i in h:
          g=list(i)
          k.append(g)
         print(tabulate(k,headers=('crop_name','crop_id'),tablefmt="fancy_grid"))
         b=input("enter crop id of the crop from the above table:-")
         cu.execute(""" SELECT c.crop_name,c.type,c.region,r.ph_level,r.moisture_level,c.ideal_climate,c.idealtemp from crops AS c
         join requirements as r ON c.crop_id = r.crop_id
         where c.crop_id = '{}'""".format(b)) 
         p=cu.fetchall()
         l=[]
         for i in p:
          g=list(i)
          l.append(g)
          print("<-----------------------------crop information--------------------------->")
         headers=['crop','Type','Region','pH Level','Moisture Level','Ideal Climate','Ideal Temp']
         print(tabulate(l, headers=headers, tablefmt="fancy_grid"))
      elif x==2:
         print("enter fertilizer type:")
         a=input("organic/inorganic-->")
         if a in ("organic","inorganic"):
            cu.execute("select fertilizer_name from fertilizers where type='{}'".format(a))
            d=cu.fetchall()
            print(d)
            b=input("enter fertilizer name-->")
            cu.execute("select fertilizer_name,usage_per_bigha,estm_price_per_50kg_bag from fertilizers where fertilizer_name='{}'".format(b))
            h=cu.fetchall()
            k=[]
            for i in h:
               g=list(i)
               k.append(g)
               print(tabulate(k,headers=('frtilizer name','usage per bigha','estimated price per 50kg'),tablefmt="fancy_grid"))
         else:
            print("Wrong input!!")
            search_page()
      elif x==3:
         print("enter pest type from below for info:-")
         a=input("insecticide/aphides/locusts/nematodes/mites-->")
         cu.execute("select pest_control_method,charges_per_bigha from pest_control where pest_type='{}'".format(a))
         q=cu.fetchall()
         '''w=[]
         for i in q:
           g=list(i)
           w.append(g)'''
         print(tabulate(list(q),headers=('pest control method','charges per bigha'),tablefmt="fancy_grid"))
      elif x==4:
         cu.execute('select crop_name,crop_id from crops')
         h=cu.fetchall()
         k=[]
         for i in h:
          g=list(i)
          k.append(g)
         print(tabulate(k,headers=('crop_name','crop_id'),tablefmt="fancy_grid"))
         b=input("enter crop id of the crop from the above table:-")
         cu.execute("select water_level,sources from irrigation_source where crop_id='{}'".format(b))
         r=cu.fetchall()
         o=[]
         for i in r:
           g=list(i)
           o.append(g)
         print(tabulate(o,headers=('WATER LEVEL','SOURCE'),tablefmt="fancy_grid"))
      elif x==5:
         cu.execute("select crop_name,crop_id from crops")
         h=cu.fetchall()
         k=[]
         for i in h:
            g=list(i)
            k.append(g)
            print(tabulate(k,headers=('crop_name','crop_id'),tablefmt="fancy_grid"))
         b=input("enter crop id of the crop from the above Table:-")
         cu.execute("select market_sales,year,total_qty_sold from market where crop_id='{}'".format(b))
         h=cu.fetchall()
         k=[]
         for i in h:
             g=list(i)
             k.append(g)
             print(tabulate(k,headers=('market_sales','year','total_qty_sold'),tablefmt="fancy_grid"))
      elif x==6:
         cu.execute('select name from tool_usage')
         h=cu.fetchall()
         print(h)
         b=input('enter the tool name for info-->')
         cu.execute("select usage1 from tool_usage where name='{}'".format(b))
         a=cu.fetchall()
         for i in a:
            print(i[0])
      elif x==7:
         cu.execute('select scheme_name from schemes')
         h=cu.fetchall()
         print(h)
         b=input('enter the scheme name for info-->')
         cu.execute("select government,key_benefits from schemes where scheme_name='{}'".format(b))
         c=cu.fetchall()
         k=[]
         for i in c:
           g=list(i)
           k.append(g)
         print(tabulate(k,headers=('government','key_benefits'),tablefmt="fancy_grid"))
      elif x==8:
         login_page()
login_page()
m.close()
