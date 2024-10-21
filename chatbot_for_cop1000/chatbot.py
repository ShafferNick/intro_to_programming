import ephem

# Global variable to store user input recommendations
recommendations = {
    'mexican': 'For Mexican cuisine, try Papi Chulo\'s in Jupiter.',
    'indian': 'For Indian cuisine, try Aroma Indian Cuisine in West Palm Beach.',
    'italian': 'For Italian cuisine, try EVO in Tequesta.',
    'cuban': 'For Cuban cuisine, try Tropical Bakery in Lake Worth.',
    'thai': 'For Thai cuisine, try Thai Lotus in Jupiter.',
    'chinese': 'For Chinese cuisine, try Black Bird in Tequesta or Lemongrass Hot Pot down in Boca Raton.'
}

cuisines = list(recommendations.keys())
user = None


def whos_my_user():
    global user
    user = input("Morpheus: Can we start with a name for me to call you? ")
    if not user.strip():
        raise ValueError('Sorry bub, that\'s not a name...')
    return user


def moon_in_fl():
    global user
    try:
        observer = ephem.Observer()
        observer.lat = '25.7617'
        observer.lon = '-80.1918'

        moon = ephem.Moon(observer)
        phase = moon.phase

        if phase < 1.0:
            phase_description = "New Moon"
        elif 1.0 <= phase < 49.9:
            phase_description = "Waxing Crescent"
        elif 50.0 <= phase < 99.9:
            phase_description = "First Quarter"
        elif 100.0 <= phase < 149.9:
            phase_description = "Waxing Gibbous"
        elif 150.0 <= phase < 199.9:
            phase_description = "Full Moon"
        elif 200.0 <= phase < 249.9:
            phase_description = "Waning Gibbous"
        elif 250.0 <= phase < 299.9:
            phase_description = "Last Quarter"
        else:
            phase_description = "Waning Crescent"

        return f"So {user}, the current phase of the moon is {phase_description}."
    except Exception as e:
        return f'Whoops, I couldn\'t get the moon phase, likely due to an error with the ephem package installation. Sorry {user}'


def top_restaurants(cuisine):
    cuisine = cuisine.lower()
    if cuisine in recommendations:
        return recommendations[cuisine]
    else:
        return None


def new_restaurant(cuisine, restaurant_name, location):
    recommendations[cuisine] = (
        f"For {cuisine.capitalize()} cuisine, try {restaurant_name.capitalize()} in {location.capitalize()}.")
    if cuisine not in cuisines:
        cuisines.append(cuisine)


def good_yoga(body_area):
    global user
    yogasanas = {
        'head & neck': 'For head and neck, try the following: \n'
                       'Neck circles, then side to side.\n'
                       'Chin to shoulder, slow and steady - inhale chin to center, exhale chin to shoulder.\n'
                       'For advanced practitioners - try plow and headstand for a challenge.\n',

        'back & core': 'For back & core, try these: \n'
                       'Sphinx, then cobra, then Upward facing dog, relaxing between each transition.\n'
                       'Supported Bridge, and for a challenge - try lifting your legs off the ground!\n'
                       'For the advanced, wheel pose - also known as bow pose, or unsupported bridge.\n',

        'shoulders & legs': 'For the limbs: \n'
                            'The full cow-faced pose is an ultimate starter. Follow it with eagle pose, then goddess.'
                            'Half split, followed by any of the warrior poses you want.'
                            'You can finish the sequence with some gentle jumps and shaking!'
    }

    return f"Hi {user}, {yogasanas.get(body_area.lower(), 'Pick one that I mentioned! Sheesh, I can only do so much here...')}"


def greetings():
    print('''Morpheus: Hello, I'm Morpheus, your friendly neighborhood chatbot with severely limited functionality. You can ask me about the current phase of the moon from South Florida, my go-to restaurants in South Florida, or yoga for your head & neck, back & core, or shoulders & legs. 
    \n Give it a shot, I'll do my best to respond! 
    \n If you want to end the discussion, just say 'bye'.''')
    
    print('''\nI'm trying to be as dynamic as possible without using any type of training, or external libraries for responses, so please state something within the following to get the best response:
        \n 'moon phase' -- I'll give you the current phase of the moon, as seen in South Florida.
        \n 'head & neck' | 'back & core' | 'shoulders & legs' -- I'll give you a series of yoga poses to try for those areas of the body!
        \n 'indian' -- Say some type of cuisine. If I have the cuisine in my list, I'll give you a great restaurant in South Florida! If not, you can give me a restaurant and location, and I'll add it to the list!
        ''')


def morpheus_the_first():
    global user
    whos_my_user()

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input == 'bye':
            print(f'Morpheus: Toodaloo {user}! Was great talking to ya!')
            return False

        elif 'moon phase' in user_input:
            print(moon_in_fl())

        elif 'restaurant' in user_input:
            found = False
            for cuisine in cuisines:
                if cuisine in user_input:
                    print(top_restaurants(cuisine))
                    found = True
                    break

            if not found:
                print(f'Sorry {user}, no info on that cuisine. But if you know a restaurant in South Florida with that cuisine, please tell me and I\'ll add it! Please be nice because I literally do NOT have the capacity to try and catch all the errors that could come up here...')
                cuisine = input(
                    'Cuisine type (e.g., Mexican, Indian): ').strip().lower()
                restaurant_name = input('Restaurant name: ').strip()
                location = input('Location in South Florida: ').strip()
                new_restaurant(cuisine, restaurant_name, location)
                print(top_restaurants(cuisine))

        elif any(body_area in user_input for body_area in ['head & neck', 'back & core', 'shoulders & legs']):
            area = next(body_area for body_area in [
                'head & neck', 'back & core', 'shoulders & legs'] if body_area in user_input)
            print(good_yoga(area))
        else:
            print(
                f'Morpheus: Sorry {user}, I didn\'t understand that. Try asking about the moon phase, restaurants, or yoga exercises in the aforementioned areas.')


def main():
    greetings()
    morpheus_the_first()


if __name__ == "__main__":
    main()
