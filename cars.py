import json

class Cars():

    id=0
    like = 0
    coment=None
    FILE='car_list.json'
    body_type = ("sedan", "universal", "cupe", "hatchback", "minivan", "jeep", "pickup")
    def __init__(self,marka,model,year,volume_of_engine,color,body_type,mileage,price):
        self.marka=marka
        self.model=model
        self.year=year
        self.volume_of_engine=volume_of_engine
        self.color=color
        self.mileage=mileage
        self.price=price
        if body_type in Cars.body_type:
            self.body_type = body_type
        else:
            raise Exception("Car 'body type' is not valid")
        self.send_car_to_json()

    @classmethod
    def get_car_id(cls):
        cls.id+=1
        return cls.id

    @classmethod
    def get_data(cls):
        with open(cls.FILE) as file:
            return json.load(file)
    
    @staticmethod
    def get_one_car(data,id):
        car=list(filter(lambda x:x['id']==id,data))
        if not car:
            return 'There is no such a product'
        return car[0]

    @classmethod
    def send_data_to_json(cls,data):
        with open(cls.FILE,'w') as file:
            json.dump(data,file)

    def send_car_to_json(self):
        data=Cars.get_data()
        car={
            'id':Cars.get_car_id(),
            'marka':self.marka,
            'model':self.model, 
            'year':self.year, 
            'volume_of_engine':self.volume_of_engine, 
            'color':self.color, 
            'body_type':self.body_type, 
            'mileage':self.mileage, 
            'price':self.price,
            'like':Cars.like,
            'coment': Cars.coment
            }
        data.append(car)
        
        with open(Cars.FILE,'w') as file:
            json.dump(data,file)
        return {'status':'201','msg':car}

    @classmethod
    def retrieve_data(cls,id):
        data=cls.get_data()
        car=cls.get_one_car(data,id)
        return car

    @classmethod
    def delete_data(cls,id):
        data=cls.get_data()
        car=cls.get_one_car(data,id)
        if type(car)!=dict:
            return car

        index=data.index(car)
        data.pop(index)
        cls.send_data_to_json(data)
        return{'status':'204','msg':'Deleted'}


    @classmethod
    def update_data(cls,id, **kwargs):
        data=cls.get_data()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return{'status':'200','msg':'Updated'}

    @classmethod
    def delete_data(cls,id):
        data=cls.get_data()
        car=cls.get_one_car(data,id)
        if type(car)!=dict:
            return car

        index=data.index(car)
        data.pop(index)
        cls.send_data_to_json(data)
        return{'status':'204','msg':'Deleted'}
    

    @classmethod
    def like_(cls, id):
        data = cls.get_data()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(like = 1)
        cls.send_data_to_json(data)
        return {'status':'200','msg':'liked'}
    
    @classmethod
    def dislike(cls, id):
        data = cls.get_data()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(like = 0)
        cls.send_data_to_json(data)
        return {'status':'200','msg':'disliked'}
    

    @classmethod
    def coments(cls,id, **kwargs ):
        data=cls.get_data()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return{'status':'200','msg':'comented'}





with open(Cars.FILE,'w') as file:
    json.dump([], file)





def main():
    print('1)Create a car\n2)Get data about all the cars\n3)Retrieve data about one car\n4)Update car\n5)Delete car\n6)Do you want like some cars\n7)Comented\n8)Exit')
    a=int(input('Выберите действие:'))
    if a == 1:
        brand=input('Brand:')
        model=input('Model:')
        year=int(input('Year of issue:'))
        volume=float(input('Engine volume:'))
        color=input('Color:')
        body=(input('Body: '))
        mileage=int(input('Milage:'))
        price=float(input('Price:'))
        Cars(brand, model, year, volume,color, body, mileage, price).send_car_to_json
        q=input('do u want to continue?(1-yes,2-no)')
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
    elif a==2:
        print(Cars.get_data())
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()

    elif a==3:
        object=int(input('Enter object index:'))
        print(Cars.retrieve_data(object))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
        
    elif a==4:
        id=int(input('Enter object index:'))
        kwargs = {}
        obj = input('What do you want to change?')
        val = input('What value do you want to change: ')
        kwargs[obj] = val
        print(Cars.update_data(id, **kwargs))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
        
    elif a==5:
        id=int(input('Enter object index:'))
        print(Cars.delete_data(id))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
    elif a == 6:
        id = int(input('Enter object index:'))
        print(Cars.like_(id))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
    elif a==7:
        id=int(input('Enter object index:'))
        kwargs = {}

        com = input('What coment do you want to add: ')
        kwargs['coment'] = com
        print(Cars.coments(id, **kwargs))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()

    elif a == 8:
        print('Okay bye!')
        
    else:
        print('Error')
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
        
    


main()