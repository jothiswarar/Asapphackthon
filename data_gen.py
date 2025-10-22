import csv
import random

# A dictionary where keys are the intents (labels) and values are lists of sample sentences (text).
# Each intent has 10 sample utterances.
DATA = {
    "Cancel Trip": [
        "I need to cancel my flight immediately.",
        "How can I cancel my upcoming trip to Denver?",
        "Please cancel my booking, reference number a4b5c6.",
        "I want a full refund for my flight.",
        "The trip is off, need to cancel everything.",
        "What's the process for cancelling a flight I booked online?",
        "Can you help me cancel my reservation?",
        "My plans have changed, I must cancel my flight.",
        "Need to cancel my ticket for next Tuesday.",
        "Cancel flight to JFK.",
    ],
    "Cancellation Policy": [
        "What is your cancellation policy?",
        "How much will it cost to cancel my flight?",
        "Will I get a refund if I cancel my ticket?",
        "Tell me about the 24-hour cancellation rule.",
        "Are there any fees for cancelling a flight?",
        "Can I get a travel credit if I cancel?",
        "What's the policy on cancelling basic economy tickets?",
        "How late can I cancel my flight without a penalty?",
        "Show me the cancellation terms and conditions.",
        "If I cancel, do I lose all my money?",
    ],
    "Carry On Luggage Faq": [
        "How many carry-on bags am I allowed?",
        "What are the size limits for a carry-on?",
        "Can I bring a backpack and a small suitcase?",
        "Is my laptop bag considered a personal item?",
        "What's the weight limit for carry-on luggage?",
        "Can I bring my guitar as a carry-on?",
        "Are liquids allowed in my carry-on?",
        "Do you charge for carry-on bags?",
        "How big can my personal item be?",
        "Can my carry-on fit in the overhead bin?",
    ],
    "Change Flight": [
        "I need to change my flight date.",
        "Is it possible to switch to an earlier flight?",
        "How can I change the destination of my booking?",
        "I want to rebook my flight for a different day.",
        "What are the fees for changing a flight?",
        "Can I change my flight online?",
        "Need to postpone my trip by one week.",
        "I booked the wrong date, can you help me fix it?",
        "How do I change the time of my flight?",
        "Move my flight from the 15th to the 18th please.",
    ],
    "Check In Luggage Faq": [
        "How much does it cost to check a bag?",
        "What's the weight limit for checked baggage?",
        "How many bags can I check?",
        "Are there discounts for checking bags online?",
        "What are the fees for an overweight bag?",
        "Can I check a box instead of a suitcase?",
        "Do I have to pay for my first checked bag?",
        "How big can my checked luggage be?",
        "I have a second bag to check, how much is it?",
        "What's the policy on checked luggage?",
    ],
    "Complaints": [
        "I want to file a complaint about my recent flight.",
        "My experience was terrible, I need to speak to a manager.",
        "The flight attendant was very rude.",
        "My flight was delayed for 5 hours with no explanation.",
        "I am very unhappy with the service I received.",
        "How do I submit a formal complaint?",
        "The plane was dirty and uncomfortable.",
        "I was charged an incorrect fee and I'm very upset.",
        "This is unacceptable, I demand a resolution.",
        "I need to report a problem with a staff member.",
    ],
    "Damaged Bag": [
        "My suitcase was damaged during the flight.",
        "The airline broke my bag, what do I do?",
        "How do I report a damaged piece of luggage?",
        "The wheel on my suitcase is broken.",
        "My bag came out on the carousel completely cracked.",
        "Can I get compensation for my damaged luggage?",
        "I need to file a claim for a broken bag.",
        "Your baggage handlers destroyed my suitcase.",
        "There's a huge tear in my luggage.",
        "Who do I talk to about a damaged bag?",
    ],
    "Discounts": [
        "Do you offer any discounts for students?",
        "Are there any senior citizen discounts available?",
        "I have a promo code, where can I apply it?",
        "Is there a discount for military personnel?",
        "How can I find the cheapest flights?",
        "Do you have any group booking discounts?",
        "Any deals for flying on a Tuesday?",
        "I'm looking for a discount on my next flight.",
        "Are there coupons for flights to Hawaii?",
        "Can I get a discount for booking a round trip?",
    ],
    "Fare Check": [
        "How much is a flight to San Francisco?",
        "Can you check the price of a ticket to Miami next month?",
        "What is the cheapest fare available for this route?",
        "I want to check the price for a one-way ticket.",
        "What's the cost of a business class seat?",
        "How much for a flight from LAX to ORD?",
        "Can you give me a fare estimate?",
        "Check flight prices for December.",
        "What's the fare for two adults?",
        "How much would it cost to add a person to my booking?",
    ],
    "Flight Status": [
        "Is flight UA456 on time?",
        "What is the status of my flight from New York to London?",
        "Can you tell me if my flight is delayed?",
        "Where is flight BA288 right now?",
        "Has my flight to Chicago departed yet?",
        "What gate is my flight leaving from?",
        "Check status for flight AA123.",
        "My flight is supposed to land soon, is it on schedule?",
        "Is the 3pm flight to Atlanta delayed?",
        "Flight status update for QR705 please.",
    ],
    "Flights Info": [
        "Do you have a direct flight to Seattle?",
        "What time are the flights to Las Vegas tomorrow?",
        "Can you tell me about the inflight amenities?",
        "Is there Wi-Fi on the plane?",
        "What kind of aircraft is used for the flight to Dubai?",
        "How long is the flight from Boston to Dublin?",
        "Do you serve meals on this flight?",
        "What are the flight options for this route?",
        "Tell me more about flight number DL987.",
        "What is the flight duration?",
    ],
    "Insurance": [
        "Should I buy travel insurance for my trip?",
        "What does your travel insurance cover?",
        "How much does flight insurance cost?",
        "Can I add insurance to my booking now?",
        "What happens if I miss my flight, am I covered by insurance?",
        "Does insurance cover trip cancellation?",
        "I need to make a claim on my travel insurance.",
        "Tell me about the insurance options.",
        "Is my luggage insured?",
        "Does the insurance cover medical emergencies?",
    ],
    "Medical Policy": [
        "Can I travel with my medication?",
        "I need to bring a portable oxygen concentrator on board.",
        "What is your policy for passengers with disabilities?",
        "Do I need a doctor's note to fly while pregnant?",
        "Can I bring my own wheelchair on the plane?",
        "I have a severe nut allergy, what is your policy?",
        "Are the flight attendants trained for medical emergencies?",
        "I need assistance boarding the aircraft.",
        "What is the procedure for traveling with medical equipment?",
        "Do you provide medical assistance at the airport?",
    ],
    "Missing Bag": [
        "My luggage did not arrive, what should I do?",
        "How do I report a lost bag?",
        "My suitcase is missing.",
        "I can't find my bag on the carousel.",
        "Can you track my missing luggage?",
        "What's the status of my lost baggage claim?",
        "The airline lost my bags, I need help.",
        "I need to file a report for a missing suitcase.",
        "How long does it usually take to find a lost bag?",
        "My bag with reference tag 12345 is lost.",
    ],
    "Pet Travel": [
        "Can I bring my dog in the cabin with me?",
        "What is your policy on traveling with pets?",
        "How much does it cost to fly with a cat?",
        "Are there any breed restrictions for pet travel?",
        "Do I need a health certificate for my pet?",
        "What are the requirements for a pet carrier?",
        "Can my pet travel as checked baggage?",
        "I need to book a flight for myself and my dog.",
        "Are emotional support animals allowed?",
        "How do I add a pet to my reservation?",
    ],
    "Prohibited Items Faq": [
        "Can I bring a lighter on the plane?",
        "Are lithium batteries allowed in checked luggage?",
        "Can I pack scissors in my carry-on?",
        "What items are not allowed on a flight?",
        "Is it okay to bring food through security?",
        "Can I carry my power bank with me?",
        "What are the rules for transporting firearms?",
        "Are there any restrictions on liquids?",
        "Can I bring my pocket knife?",
        "List of prohibited items please.",
    ],
    "Seat Availability": [
        "Are there any window seats left?",
        "Can I check the seat map for my flight?",
        "I'd like to select my seat now.",
        "How much does it cost to choose a seat?",
        "Are there any seats available in business class?",
        "Can you find two seats together for me?",
        "What seats are open on flight F234?",
        "I want a seat with extra legroom.",
        "Can I upgrade my seat?",
        "Show me the available seats.",
    ],
    "Sports Music Gear": [
        "Can I check my golf clubs?",
        "How do I travel with a bicycle?",
        "What are the fees for checking a surfboard?",
        "Can I bring my cello as a carry-on?",
        "Is there a special policy for sports equipment?",
        "How should I pack my skis for a flight?",
        "I need to fly with my guitar.",
        "What is the cost for oversized baggage like a snowboard?",
        "Are there any restrictions on checking fishing gear?",
        "Can I bring my bowling ball on the plane?",
    ],
}


def generate_dataset(filepath="airline_support_dataset.csv"):
    """
    Generates a CSV dataset from the DATA dictionary.

    Args:
        filepath (str): The name of the CSV file to create.
    """
    header = ["text", "label"]

    # Flatten the data from the dictionary into a list of [text, label] pairs
    rows = []
    for label, texts in DATA.items():
        for text in texts:
            rows.append([text, label])

    # Shuffle the rows to ensure the data is not ordered by intent
    random.shuffle(rows)

    try:
        with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Write the header
            writer.writerow(header)
            # Write the data rows
            writer.writerows(rows)
        print(f"Successfully created '{filepath}' with {len(rows)} rows.")
    except IOError as e:
        print(f"Error writing to file {filepath}: {e}")


if __name__ == "__main__":
    # When the script is executed, it will generate the CSV file.
    generate_dataset()
