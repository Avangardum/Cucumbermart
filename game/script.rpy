define l = Character("Linda")
define s = Character("Sophie")
define c = Character("Connor")
define e = Character("Elliot")
define p = Character("Police Officer")



label start:

    scene bg street

    "I am Linda Stevenson, 35 years old."
    "My husband John died 1 year ago leaving me with our 12 years old daughter Sophie."
    "For most of my life I worked in a grocery store chain Titan Hypermart. I went all the way from a regular employee 
        to a store manager."
    "I love my job, however the company sometimes makes decisions that many consider to be immoral: mistreating workers,
        working with questionable suppliers, etc. They care about money above everything else and this sometimes makes
        me feel disappointed."
    "Of course I was doing what I could to make my store a better place to work at, but, unfortunately, not all things
        were under my control"
    "But now things are going to change, because I will open my own store! I just moved to Sunrise City, a city
        recently founded near a newly discovered oilfield. I bought a building for a store with my saved money."
    "The store is named Cucumbermart. Sophie came up with this name. It's almost ready to open."

    scene bg cucumbermart
    show linda at left
    show sophie at right
    with dissolve
    
    l "Finally! All of the preparations are done. The shop is ready to open tomorrow."
    s "Great job, mom! You worked very hard and Cucumbermart looks amazing. I love it."
    l "Thanks, Sophie. I'm glad to hear that."

    menu:

        s "By the way, I think it would be even better if we added a big vase with flowers on the floor. It would look 
            very nice. What do you think?"

        "Buy red roses":

            l "Nice idea! I'll buy some red roses."
            s "Cool! Thank you!"
            $ cucumbermartBackground = "bg cucumbermart roses"

        "Buy purple orchids":

            l "Nice idea! I'll buy some purple orchids."
            s "Cool! Thank you!"
            $ cucumbermartBackground = "bg cucumbermart orchids"

        "Buy yellow tulips":

            l "Nice idea! I'll buy some yellow tulips."
            $ cucumbermartBackground = "bg cucumbermart tulips"
            s "Cool! Thank you!"

        "Don't buy flowers":

            l "No, I don't think it's a good idea. I don't think that flowers will fit in here. Plus someone could knock
                them over."
            s "Oh, okay. I understand."
            $ cucumbermartBackground = "bg cucumbermart"

    scene expression cucumbermartBackground with dissolve
    
    "Tomorrow Cucumbermart opened. A lot of people cane to the store, it became quite popular. Profit was good and people
        liked the store. I was happy."
    
    jump hungryHearts



label hungryHearts:

    "Two weeks after the store opening"

    show connor at left
    show linda at right
    with dissolve

    c "Greetings. I'm Connor Morgan. I work for the Hungry Hearts Foundation. I'd like to talk to the owner of this store."
    l "I'm Linda Stevenson, the owner of this store. What can I do for you?"
    c "Our organization helps to feed the homeless and poor. There are a lot of people in the country who experience food
        insecurity while tons of food are thrown away every day."
    l "I see. That's... concerning."
    
    menu:

        c "I'd like to ask you to help our organization by donating expired food from your store. We'll distribute it to those
        who need it. Will you help us?"

        "Agree":
            jump hungryHeartsAgree
            
        "Refuse":
            jump hungryHeartsRefuse



label hungryHeartsAgree:

    l "Yes, I'll help you. I'll donate expired food to your organization."
    c "Thank you very much! You're doing a good thing."

    $ donatedFood = True

    scene expression cucumbermartBackground with dissolve

    "One week later"

    show policeOfficer at left
    show linda at right
    with dissolve

    p "Good afternoon. Are you Linda Stevenson?"
    l "Yes, I am."
    p "I came to inform you that there was a lawsuit filed against you. You was providing people expired food and it
        caused food poisoning. You will have to visit a court in two days."
    l "Oh, I understand. I will be there."
    
    hide policeOfficer with dissolve

    "Shit! That't not good."
    "How could this happen? I know that food is actually safe to eat even a few days after the expiration date. I only 
    donated the food that expired in that exact day and Connor told me that they use it in a couple of days."

    scene black with dissolve

    "In 2 days the trial occurred. They declared me and the Hungry Hearts Foundation guilty in distribution of unsafe food.
        The Hungry Hearts Foundation was forced to close. I got off with a fine. The fine was pretty big, but at least
        my shop could continue to work as before."

    scene bg street evening with dissolve

    "Later this evening"

    show linda at right with dissolve

    l "Oof... What a day."

    show connor at left with dissolve

    c "Hello, Linda. I came to say sorry for involving you in this. Things went really bad for us."
    l "Hello, Connor. That's a tough situation indeed. But I still wonder how could this happen even though all of us
        took measures to ensure safety."
    c "I don't know. I'm sure that we did everything right. I think that someone is trying to frame us. Our organization
        was disliked by some people. I know that Titan Hypermart executives were among them. They say that such
        organizations cause them to lose profits."
    c "What a bunch of rich assholes. They don't care about people. They only care about money. I have a strong feeling
        that they are behind this. They probably bribed some of our recipients to fake food poisoning and file a lawsuit."
    l "I see. That's a very serious accusation. But I think you may be right. I know that they are capable of such things."
    
    menu:

        c "Unfortunately, this is just an assumption. We don't have any evidence. Once again sorry for bothering you."

        "You shouldn't apologize.":

            l "You shouldn't apologize. You didn't do anything wrong. You were doing a right thing."
            c "Thank you for you understanding. You have a kind heart, Linda. Goodbye."

        "...":

            c "Goodbye."

    scene bg home with dissolve

    "The next day."

    jump teddyBear



label hungryHeartsRefuse:

    l "Sorry, but I can't help you. I have my reasons."
    c "I see. I'm disappointed. I thought you were a good person."

    $ donatedFood = False

    scene bg home with dissolve

    "10 days later."

    jump teddyBear



label teddyBear:

    "qqq"