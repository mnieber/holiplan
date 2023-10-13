MS 1: A user can create a (empty) holiday plan

1.1 The user opens the holiday-planner.
1.1.1 For this milestone, there is no user registration
1.2 The user can choose to create a new holiday plan
1.2.1 The user enters the holiday name
1.2.2 A key for the holiday is created.
1.3 The user can choose to access an existing holiday plan
1.3.1 In this case, they enter the key of their holiday plan.

MS 2: A user can add destinations to their plan

2.1 The user chooses "Add destination"
2.2 They enter the name of their destination
2.2.1 If the name is ambiguous, the user is asked to specify additional information
2.2.2 For example, they may be asked for the continent, country or region
2.2.3 When we present a list of possible destinations, then the one that is closest to an existing destination in the plan is suggested first.
2.3 They enter the date for reaching this destination
2.4 The destination is inserted into the holiday plan
2.4.1 Destinations are sorted on date

MS 3: The user sees the expected weather at each destination

3.1 The expected weather is shown when the user is adding the destination (before actually adding it)
3.2 The expected weather is also shown for every destination that is in the plan
3.3 The expected weather is based on the current weather forecast. It's not some average over previous years.
3.3.1 Therefore we should not store weather forecasts in the database, but always calculate fresh ones.
