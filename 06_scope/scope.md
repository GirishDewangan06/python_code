|-------------------------------------------------|
| |username|----->[chaiaurcode]                   |#here "chaiaucode" memory ref taken by
|                                                 |  "username"
|                            (Function Ghar)      | 
|   hitesh               |-----------------|      | 
|                        |  hitesh'        |      |hitesh'& bal access can not taken by  
|                        |                 |      |                               hitesh
|                        |                 |      |
|          |a|           |       |'hitesh| |      |but, 'hitesh access can taken by hitesh'
|                        ||bal|  |'hitesh| |      |internally in function block(ghar)scope
|                        |                 |      |or namespace.
|                        |                 |      | 
|                        |                 |      |but, a ref can taken by hitesh' and  
|                        |_________________|      |                     hitesh , globally
|                                                 |
|                                                 |
|_________________________________________________|