import unittest
import camelcase

# def myfunc():
#   try:
#     print('first line')

#     #print(x)
#     x = "hello"
#     if not type(x) is int:
#       raise TypeError("Only integers are allowed")

#     c = camelcase.CamelCase()
#     txt = "hello world"
#     print(c.hump(txt))
#   except:
#     print("Something else went wrong")
# myfunc()


def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)
    def test_add_fish_to_aquarium_exception(self):
        too_many_fish = ["shark"] * 25
        with self.assertRaises(ValueError) as exception_content:
            add_fish_to_aquarium(fish_list=too_many_fish)
        self.assertEqual(
          str(exception_content.exception),
          "A maximum of 10 fish can be added to the aquarium"
        )
