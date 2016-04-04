# flagon

A simple API in Python using [Bottle](http://bottlepy.org/) that consumes JSON messages and pushes the content to SMSD for delivery.

As always, very much a work in progress.

## How To Use

Simplistically you simply **PUT** a JSON message to the /sendsms endpoint. The format is a subset of the [smstools3 SMS file format](http://smstools3.kekekasvi.com/index.php?p=fileformat).

``` json
{
    "recipient": 441234567890,
    "body": "Test Message"
}
```
