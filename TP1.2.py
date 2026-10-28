total_seconds = 9875
hour = total_seconds //3600 
minute = (total_seconds % 3600)//60
second = (total_seconds % 60)
print(f"9875 secondsn = {hour:} h {minute:} m {second} s")

print("checkk = ",(hour*3600)+(minute*60)+second == total_seconds)