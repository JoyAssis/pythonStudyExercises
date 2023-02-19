seconds_str = input("Type the seconds to convert: ")
total_sec = int(seconds_str)

hours = total_sec // 3600
sec_remainder = total_sec % 3600
min = sec_remainder // 60
sec_remainder_final = sec_remainder % 60

print(hours, "hours, ", min, "minutes and ", sec_remainder_final, "seconds.")