- Running the application will utilize a command line tool that will autodetect if a setup is required (or recommended)

- If and after setup has been complete, use a command line tool allowing the user to 
initiate, stop, monitor the auto staking.

    -- Setup:
        -- Generate a timestamp file in the data folder used to track staking events.
            -- data/staking_events.csv
    -- Initiate:
        -- Asks user for the password to allow access to the keplr wallet 
            -- (encoded and saved in ram, not harddrive; 
                                simply meaning do not save this password, 
                                keep it as a variable to increase security, 
                                still not secure tho, thats why we need to encrypt it, 
                                still not secure tho as the signature used to encrypt 
                                will also be in ram. But this is secure for now (not really for a good hacker).)

        -- Set timeframe for auto staking

        -- Set amount to leave behind when auto staking, so theres enough left to retrieve awards again.

        -- Set speed at which the re-staking transaction should occur
            -- Faster costs more, IgnoreAmount needs to be higher in this case.
            -- Low by default as it is the cheapeast option, transactions are fast on akash anyway.

    -- Active: The state in which the application is running in the background determining if it should restake or not.
        -- Command line tool stays alive in this case (for now)


- Application will need to launch a browser to stake / restake.
    -- Only lauch the browser when a staking event occurs.

[DEPRECATED: DO NOT DO. BUT READ FIRST]
- User will need to manually initiate the first staking event to prime the system.
    - Avoids error of staking if recently staked before the application is started for the first time.
    -- Avoid the above by calculating wether or not staking is possible (lack of funds) 
    --- if possible the applications first staking event can be automatically generated.

- The first time a staking event occurs generate a timestamp tracking file.
    -- This file will be used to determine when the last staking happened and if the application should stake or not
    --- (Optional) Add event data such as AmountBeforeStaking AmountAfterStaking, StakingCost, etc.

- After a specified time period, instantiate a browser instance and preform the restaking event.
    - Restaking event will add to the existing timestamp file.
    - The specified time period should be checked against the last entry in the timestamp file


-