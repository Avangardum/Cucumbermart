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
    
    "Tomorrow Cucumbermart opened. A lot of people came to the store, it became quite popular. Profit was good and people
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

        "Help":
            jump hungryHeartsAgree
            
        "Don't help":
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

    show linda at left
    show sophie at right
    with dissolve

    s "Mom! Mom! Mom!"
    l "What's up, Sophie?"
    
    if donatedFood:

        s "I saw a huge teddy bear in a toy store. It's so cute! Can you buy it for me, please?"

        jump teddyBearNoMoney

    menu:

        s "I saw a huge teddy bear in a toy store. It's so cute! Can you buy it for me, please?"

        "Buy the huge teddy bear":

            jump teddyBearAgree

        "Buy a small teddy bear instead":

            jump teddyBearRefuse


label teddyBearAgree:

    l "Of course, Sophie. I'll buy it for you."
    s "Thank you, mom! You're the best!"
    l "You're welcome, honey."

    jump visitByElliot



label teddyBearRefuse:

    l "No, Sophie. I can't buy it for you. It cost very much and you will probably get bored of it in a few days. How about
        I buy you a smaller teddy bear? And we can buy some other toys too."
    s "Well, okay. I guess it's fine."

    jump visitByElliot



label teddyBearNoMoney:

    l "I'm sorry, Sophie. I can't buy it for you. I'm really low on money after that fine and I can't afford it."
    s "Oh, well, I see. It's sad that they fined you for helping people in need."
    l "Yeah, I know. But I'm sure that everything will be fine."

    jump visitByElliot



label visitByElliot:

    scene expression cucumbermartBackground with dissolve

    "The next day"

    show linda at right
    show elliot at left
    with dissolve

    e "Hello, Linda. Nice store you have here. Looks very nice and cozy. It's clear that the store is run by a true
        professional."
    l "Thank you. I'm glad to hear that. What can I do for you?"

    menu:

        e "My name is Elliot Saunders. I'd like to ask you how is your business going."

        "Good":

            l "It's going well. The store is quite popular and I'm making a good profit."
            e "I'm glad to hear that. You managed to take a good place in the market as the city is new and there are not
                many stores here yet. But I think that the competition will get tougher as more stores will open."
            e "I am from Titan Hypermart upper management. You have probably heard that we are about to open a store in
                this city. I think it would be better for all of us if we worked together."
            l "What do you mean?"
            e "We'd like to buy this store from you. It will become a part of Titan Hypermart. You will receive a lot of
                money for it. And you will be able to keep working here as a manager and get a good salary."

        "Bad":

            l "Unfortunately, it's not going very well. I have some struggles with it. But I think that the problems will
                pass and everything will get better."
            e "I see. It indeed is a challenging task to run a new business on your own. But I think that I can help you
                with that."
            l "What do you mean?"
            e "I am from Titan Hypermart upper management. We would like to buy this store from you. You will receive a lot
                of money for it. And you will be able to keep working here as a manager and get a good salary. With us you
                will surely overcome all of your struggles."
            e "Also, as you probably know, we are opening a new store in this city. If you agree, we won't have to 
                compete with each other. We will be able to work together to optimize profits of both stores."
            
    menu:

        e "So, what do you think of this offer?"

        "Sell Cucumbermart":

            l "I think it's a good offer. I'll sell the store to you."
            e "Great! I'll send you the contract. I'm sure that you won't regret this decision."

            jump titanHypermartEnding

        "Don't sell Cucumbermart":

            l "No, I'm not going to sell the store. I want to run it myself and to have full control over it."
            e "I see. That's unfortunate. I think you're making a mistake. Here is my business card. If you change your
                mind, feel free to contact me."

            jump priceDumping



label titanHypermartEnding:

    scene expression cucumbermartBackground with dissolve

    "In the next days I signed the contract and sold the store to Titan Hypermart. I kept working there as a manager.
        I have a lot of money from selling the shop and from my manager salary. My life is good and rich now."
    "But sometimes I feel bad about selling the store. After all I founded it because I wanted to run my own business,
        to have full control over it and to make the decisions that I consider to be right. But now I'm again just 
        a manager in a big corporation. And I have to follow their rules and do what they say."
    "But in the end of the day I gained a lot from this. Now I and Sophie can afford everything we want. We are living 
        a happy and comfortable life."
    "{b}Ending 1/3.{/b}"
    return



label priceDumping:

    "qqq"