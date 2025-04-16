# RedisNot
```
                                   ,----,
         ,--.    ,----..         ,/   .`|
       ,--.'|   /   /   \      ,`   .'  :        ,-.----.       ,---,.    ,---,       ,---,  .--.--.
   ,--,:  : |  /   .     :   ;    ;     /        \    /  \    ,'  .' |  .'  .' `\  ,`--.' | /  /    '.  
,`--.'`|  ' : .   /   ;.  \\.'___,/    ,'         ;   :    \ ,---.'   |,---.'     \ |   :  :|  :  /`. /  
|   :  :  | |.   ;   /  ` ;|    :     |          |   | .\ : |   |   .'|   |  .`\  |:   |  ';  |  |--`   
:   |   \ | :;   |  ; \ ; |;    |.';  ;          .   : |: | :   :  |-,:   : |  '  ||   :  ||  :  ;_     
|   : '  '; ||   :  | ; | '`----'  |  |          |   |  \ : :   |  ;/||   ' '  ;  :'   '  ; \  \    `.  
'   ' ;.    ;.   |  ' ' ' :    '   :  ;          |   : .  / |   :   .''   | ;  .  ||   |  |  `----.   \ 
|   | | \   |'   ;  \; /  |    |   |  '          ;   | |  \ |   |  |-,|   | :  |  ''   :  ;  __ \  \  | 
'   : |  ; .' \   \  ',  /     '   :  |          |   | ;\  \'   :  ;/|'   : | /  ; |   |  ' /  /`--'  / 
|   | '`--'    ;   :    /      ;   |.'           :   ' | \.'|   |    \|   | '` ,/  '   :  |'--'.     /  
'   : |         \   \ .'       '---'             :   : :-'  |   :   .';   :  .'    ;   |.'   `--'---'   
;   |.'          `---`                           |   |.'    |   | ,'  |   ,.'      '---'                
'---'                                             `---'      `----'    '---'                             
```

## TODO

- [ ] Replace `print` statements with proper logging.
- [ ] Replace blocking network calls with non-blocking alternatives. Currently, the server uses `time.sleep()` and socket timeouts to facilitate shutdown, as invoking `stop()` from another thread does not interrupt a blocking `accept()` call.
- [ ] Replace the threading model with an event-driven loop to handle multiple concurrent clients more efficiently.

## Future Enhancements

- [ ] Consider supporting Linux-specific `epoll`, with `select` as a fallback for portability.
