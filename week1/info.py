user_info={"FirstName":"Алексей","LastName":"Малашенков"}
print(user_info.get("FirstName"))
print(user_info.get("date", 1987))

var01={
    "city":"Москва",
    "temperature":20
}
var01["temperature"] = var01["temperature"] - 5
print(var01["temperature"])

var01.get("country", "Russia")
var01["date"] = "27.05.2019"
print(len(var01))