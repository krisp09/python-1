def main():
 shopping_list = ['A', 'B', 'C', 'D']
 #print(f"shopping item :{shopping_list[-1]}")
 shopping_list.pop(1)
 shopping_list.append('K')
 print(f" B removed from list pop :{shopping_list[1]}")
 len_list = len(shopping_list)
 print(f"length of the list: {len_list}")












if __name__ == '__main__':
    main()