## project progress for gregor

### What has been done:

aws and google have proper documentation and implementation into the command line and into the catalog

```commandline
cms nlp translate --provider=aws --from=en --to=de --region=eu-west-1 hello world

cms nlp translate --provider=google --from=en --to=de --region=eu-west-1 hello world
```


Azure has proper documentation and a tutorial of how to use on the command line.
Azure has a sample program that runs using the endpoints and keys found in documentation.
this program translates text.

Each service has the proper documentation to
achieve all the endpoints and secret keys needed for hybrid text translation.



### What has not been done:

implementation of azure using nlp.py still needs completed.

example:
```commandline
cms nlp translate --provider=azure --from=en --to=de --region=eu-west-1 hello world
```

documentation on docs and redocs for aws, google and azure is still to be completed.
