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

    scene expression cucumbermartBackground
    with dissolve
    
    "Tomorrow Cucumbermart opened. A lot of people cane to the store, it became quite popular. Profit was good and people
        liked the store. I was happy."
    
    jump hungryHearts

label hungryHearts:

    "One week after the store opening"

    show connor at left
    show lauren at right
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
            l "Yes, I'll help you. I'll donate expired food to your organization."
            c "Thank you very much! You're doing a good thing."
            $ donatedFood = True
            
        "Refuse":
            l "Sorry, but I can't help you. I have my reasons."
            c "I see. I'm disappointed. I thought you were a good person."
            $ donatedFood = False
        
    "qqq"
