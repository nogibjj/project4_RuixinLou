# project4_RuixinLou

This is an api application based on fast-api.

The application was built to connect to google cloud platform database, and perform data processing to the StackOverflow dataset, which merged the posts id dataset and the posts rating dataset, and sorted the merged dataset in a descending order. The output is the top four new death rate, new hopitalization rate, and new covid positive rate ordered by date descendingly.

The recent four rate information can be shown through /topfour command in the url of fast api application.

The application is pushed to AWS ECR and AWS app runner, and the aws app runner's auto deploy function is turn on, which allows the app runner to update automatically when new (updated) docker image is pushed to AWS ECR.
