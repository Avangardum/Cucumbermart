define l = Character("Linda")
define s = Character("Sophie")
define c = Character("Connor")
define e = Character("Elliot")
define p = Character("Police Officer")



label start:

    scene bg street

    "I am Linda Stevenson, 30 years old."
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

    show police_officer at left
    show linda at right
    with dissolve

    p "Good afternoon. Are you Linda Stevenson?"
    l "Yes, I am."
    p "I came to inform you that there was a lawsuit filed against you. You was providing people expired food and it
        caused food poisoning. You will have to visit a court in two days."
    l "Oh, I understand. I will be there."
    
    hide police_officer with dissolve

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

    scene bg titan_hypermart
    show linda at left
    with dissolve

    "A week later Titan Hypermart opened its shop in Sunrise city. I decided to visit it to see how it looks like."
    "It looked kinda usual. Not much different from other Titan Hypermart stores."
    l "Wait, what's that?!"
    "I looked at the prices and was shocked. They were extremely low. Even lower that I bought products from suppliers."
    "I was confused. How could they sell products at such low prices? I know that they are a big corporation and they
        have a lot of money, but still. I know that they have a lot of expenses too. They have to pay salaries to their
        employees, pay rent for the store, pay for electricity, etc."
    "Are they doing this to drive me out of business? That can be a problem."
    "I left the store with a feeling of anxiety. I was worried about my store. I was worried about my future."

    scene expression cucumbermartBackground with dissolve

    "In the following days I noticed that the number of customers in my store decreased. People were lured to Titan Hypermart
        by their low prices. I had to lower my prices too to compete with them. But I couldn't lower them as much as they
        did while still making profit. I started to lose money."
    "With each day the situation was getting worse. I was losing more and more money. Eventually my savings almost ran out."

    scene bg home night
    show linda at right
    with dissolve

    "After another anxious day I came home. I was very tired and stressed. I was sitting on the couch and thinking about
        what to do next."
    l "It can't go on like this. I'm losing money every day. I can't keep working like this. I have to do something."
    l "I can take a loan to keep the store running for some time. But if the things stay the same, I won't be able to 
        pay it back. I will go bankrupt. And it doesn't seem like the situation will change. Titan Hypermart will keep
        their low prices and I won't be able to compete with them."
    l "Otherwise I can sell the store. Of course it will hurt me to do this, to give up on my dream. But I will get a lot
        of money for it. My financial struggles will be over. And after all that seems to be the only way to save the store."
    l "..."
    l "Or is it?"
    l "Maybe if something happened to Titan Hypermart, like a fire or something..."
    l "No, that's a stupid idea. I can't do that."
    l "..."
    
    menu:

        l "So, what should I do?"

        "Take a loan":

            jump bankruptcyEnding

        "Sell Cucumbermart":

            jump sellCucumbermartLater

        "Burn Titan Hypermart":

            jump arsonPreparation



label bankruptcyEnding:

    l "I'll take a loan. I'll keep working and I'll try to find a way to save the store. After all Titan Hypermart
        can't keep their prices so low forever. I bet they are working at a loss right now. They will have to raise
        their prices eventually. And then I will be able to compete with them again."

    scene bg home with dissolve

    "Days passed by. I was working hard. I was trying to find a way to save the store. But I couldn't. Titan Hypermart
        kept their prices low. Eventually I completely ran out of money. I couldn't pay the loan back. I went bankrupt."
    "My business was over. I lost my store. And the worst thing is that Titan Hypermart ended up buying it in a bankruptcy
        auction. I was devastated."
    "I am not sure what I will do next. I really don't want to come back working for Titan Hypermart after all they did 
        to me. Maybe I should find a job in another city, in another shop. Or maybe I should change my entire career. 
        I don't know. I guess time will tell."
    "{b}Ending 2/3.{/b}"

    return



label sellCucumbermartLater:

    l "It seems like I have no other choice. I'll sell the store to Titan Hypermart."
    l "I'll call Elliot tomorrow."

    jump titanHypermartEnding
    


label arsonPreparation:

    l "I may seem stupid, but it looks like the only way to save my shop and my decency. I'll sneak into the Titan 
        Hypermart and start a fire."
    l "That's gonna be tough. I'll have to be very careful. I'll have to make sure that no one sees me. But in the end 
        those bastards won't interfere with my life anymore."

    scene black with dissolve

    "I spent the next day preparing for the arson. I bought a canister of gasoline. I also bought a mask and gloves to 
        hide my identity. I was ready to do it."

    scene bg titan_hypermart night 
    show linda at left
    with dissolve

    "In the night I sneaked into the store. I ensured that there was no one inside. I was ready to start the fire."
    "But I hesitated."
    "Should I really do this? It's a crime. I can go to jail for this. What will happen to Sophie then?"
    "What if someone gets hurt? What if someone dies? I don't want to be a murderer."
    "Maybe I should dump this idea, get home and forget about this."

    menu:

        "What should I do?"

        "Go home":

            jump arsonCancelled

        "Burn it down":

            jump arsonEnding
        


label arsonCancelled:

    "Fuck it, I'm not doing this! I must get out of here!"

    scene bg home night with dissolve

    "I returned home and got rid of all the clues."
    "I almost made a terrible mistake. But now it's all over."
    
    menu:

        "But that still leaves me with a question. What should I do with Cucumbermart?"

        "Take a loan":

            jump bankruptcyEnding

        "Sell Cucumbermart":

            jump sellCucumbermartLater



label arsonEnding:

    "I'll do what I must. Whatever it takes."
    "I spilled the gasoline around the shop."
    "Then I took a lighter and ignited it."

    show bg titan_hypermart night fire with dissolve

    "The store bursted into flames."
    "A fire alarm went off."
    "I need to get out of here."

    show bg street night
    show linda at left
    with dissolve

    "I rushed out of the shop. I ran away as fast as I could."
    "I turned around a corner when..."

    show police_officer at right with dissolve

    p "Hey! Who you are?! What are you doing here?!"
    l "I... I..."
    p "You are under arrest on suspicion of being related to the fire in the store nearby. I'm taking you to the police 
        station."
    l "No, wait! I didn't do anything! I'm innocent!"
    p "You will have a chance to prove it in court."

    scene black with dissolve

    "The court declared me guilty in arson. I was sentenced to 3 years in prison."
    "Sophie was sent to an orphanage. I don't know what will happen to her now."
    "The fire was quickly extinguished. The store was moderately damaged. Titan Hypermart repaired it and opened it again.
        Fortunately no one was hurt."
    "Titan Hypermart also seized Cucumbermart as a compensation for the damage."
    "I lost everything. I lost my store. I lost my freedom. I lost my daughter."
    "What have I done? Why did I do this? I was so stupid. I should have never done this."
    "{b}Ending 3/3.{/b}"

    return