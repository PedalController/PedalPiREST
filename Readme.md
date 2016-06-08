# WebService - Rest v1.0

## Effects

* /effects: 
 * GET. Get all effects instaled
* /effect/([^/]+):
 * GET. Get ____

## Read and update

* ```/banks```
  *  GET all banks
* ```/bank/(?P<bank>[0-9]+)/patch/(?P<patch>[0-9]+)/effect/(?P<effect>[0-9]+)/param/(?P<param>[0-9]+)```
  * GET a parameter value
  * PUT for update a parameter value
* ```/bank/(?P<bank>[0-9]+)/patch/(?P<patch>[0-9]+)/effect/(?P<effect>[0-9]+)```
  * GET a effect
  * PUT for update a effect
* ```/bank/(?P<bank>[0-9]+)/patch/(?P<patch>[0-9]+)```
  * GET a patch
  * PUT for update a patch
* ```/bank/(?P<bank>[0-9]+)```
  * GET a bank
  * PUT for update a bank
  * DELETE a bank

## Save new

* ```/bank/(?P<bank>[0-9]+)/patch/(?P<patch>[0-9]+)/effect```
  * POST a new effect. The effect index is returned
* ```/bank/(?P<bank>[0-9]+)/patch```
  * POST a new patch. The patch index is returned
* ```/bank```
  * POST a new bank. The bank index is returned
        
## Current

* ```/current/bank/(?P<bank>[0-9]+)```
 * PUT the current bank
* ```/current/patch/(?P<patch>[0-9]+)```
 * PUT the current patch
* ```/current/effect/(?P<effect>[0-9]+)```
 * PUT for toggle effect status (actived for bypassed or bypassed for actived) of the current patch
* ```/current/effect/(?P<effect>[0-9]+)/param/(?P<param>[0-9]+)```
 * PUT for set a parameter value for a effect of the current patch

## Connections
        
## Peripheral