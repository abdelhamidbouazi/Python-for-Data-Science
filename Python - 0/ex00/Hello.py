ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

tuple_temp = list(ft_tuple)
tuple_temp[1] = "Morocco!"
ft_tuple = tuple(tuple_temp);

ft_set_temp = list(ft_set);
ft_set_temp[1] = "Khouribga!";
ft_set = set(ft_set_temp);

ft_dict["Hello"] = "1337KH!";

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)