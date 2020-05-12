def calculate_pace(distance_km, hours, minutes, seconds):

    seconds += 60 * minutes
    seconds += 3600 * hours
    
    pace_min = int((seconds / distance_km) // 60)
    pace_secs = round((seconds / distance_km) % 60, 2)

    pace_string = str(pace_min) + ":" + str(pace_secs)

    return pace_string

def main():
    distance_km = float(input("Insert desired distance: "))
    hours = float(input("Insert hours you want to run: "))
    minutes = float(input("Insert minutes you want to run: "))
    seconds = float(input("Insert seconds you want to run: "))

    pace = calculate_pace(distance_km, hours, minutes, seconds)
    
    print(pace)

if __name__ == "__main__":
    main()