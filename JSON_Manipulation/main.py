import json
from datetime import datetime


data_string = '''
[
  {
    "inventory_id": 9382,
    "name": "Brown Chair",
    "type": "furniture",
    "tags": 
            [
              "chair",
              "furniture",
              "brown"
            ],
    "purchased_at": 1579190471,
    "placement": 
            {
              "room_id": 3,
              "name": "Meeting Room"
            }
  },
  {
    "inventory_id": 9380,
    "name": "Big Desk",
    "type": "furniture",
    "tags": 
            [
              "desk",
              "furniture",
              "brown"
            ],
    "purchased_at": 1579190642,
    "placement": 
            {
              "room_id": 3,
              "name": "Meeting Room"
            }
  },
  {
    "inventory_id": 2932,
    "name": "LG Monitor 50 inch",
    "type": "electronic",
    "tags": 
            [
              "monitor"
            ],
    "purchased_at": 1579017842,
    "placement": 
            {
              "room_id": 3,
              "name": "Lavender"
            }
  },
  {
    "inventory_id": 232,
    "name": "Sharp Pendingin Ruangan 2PK",
    "type": "electronic",
    "tags": 
            [
              "ac"
            ],
    "purchased_at": 1578931442,
    "placement": 
            {
              "room_id": 5,
              "name": "Dhanapala"
            }
  },
  {
    "inventory_id": 9382,
    "name": "Alat Makan",
    "type": "tableware",
    "tags": 
            [
              "spoon",
              "fork",
              "tableware"
            ],
    "purchased_at": 1578672242,
    "placement": 
            {
              "room_id": 10,
              "name": "Rajawali"
            }
  }
]
'''

data = json.loads(data_string)

#Create a Function
#===================================================================
def getAllElectronicDevice(): 
      arr = []
      for i in data:
            electronic = i['type'] == 'electronic'
            if electronic:
                  arr.append(i)
      print('All Electronic Device : ')
      json_obj = json.dumps(arr, indent=2)
      print(json_obj)

#====================================================================
def getItemInMeetingRoom():
      arr = []
      for i in data:
            meetingRoom = i['placement']['name'] == 'Meeting Room'
            if meetingRoom:
                  # arr1 = i['name']
                  arr.append(i)
      #             arr.extend(arr1)
      # listToString = ', '.join(arr)
      json_obj = json.dumps(arr, indent=2)   
      print('Items in the meeting room : ')
      print(json_obj) 

#=====================================================================
def allFurniture():
        arr = []
        for i in data:
              furniture = i['type'] == 'furniture'
              if furniture:
                    # arr1 = i['name']
                    arr.append(i)
        # listToString = ', '.join(arr)
        json_obj = json.dumps(arr, indent=2) 
        print('All of the furniture :')
        print(json_obj)
        # print(arr)

# ====================================================
def itemWithBrownColor():
        arr = []
        for i in data:
              for j in i['tags']:
                      getBrown = j == 'brown'
                      if getBrown:
                            arr.append(i)
                            # arr1 = i['name']
                            # arr.append(arr1)
        # listToString = ', '.join(arr)
        json_obj = json.dumps(arr, indent=2)
        print('Items with brown color : ')
        print(json_obj)

# ================================================================================
def getItemPurchased():
        for i in data:
              get_timestamp = i['purchased_at']
              dt_obj = datetime.fromtimestamp(get_timestamp).strftime('%d-%m-%y')
              if dt_obj == '16-01-20':
                    all_item = json.dumps(i,indent=4)
                    print(all_item)


def main():
  
        print(
          """
          1. Find items in the Meeting Room.
          2. Find all electronic devices.
          3. Find all the furniture.
          4. Find all items were purchased on 16 Januari 2020.
          5. Find all items with brown color.
          Lihat data (1-5) :
          """, end=''
        )
        inp = int(input())
        if inp == 1:
              getItemInMeetingRoom()
        elif inp == 2:
              getAllElectronicDevice()
        elif inp == 3:
              allFurniture()
        elif inp == 4:
              getItemPurchased() #data [0] dan [1] = 16jan20
        elif inp == 5:
              itemWithBrownColor()
        else:
              print("Input must be an integer")
main()
