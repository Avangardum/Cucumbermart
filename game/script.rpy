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
        me feel dissapointed."
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
        s "By the way, I think it would be even better if we added a big vase with flowers on the floor. It would look very 
            nice. What do you think?"
        "Choice 1":
            "c1"
        "Choice 2":
            "c2"
        