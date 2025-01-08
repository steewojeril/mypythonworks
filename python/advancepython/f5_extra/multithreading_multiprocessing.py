
'''

-Thread: A tiny task inside a program. You can think of it as a worker doing part of the work.
For example, in a web browser, one thread could be downloading a webpage, another thread could be showing the webpage to you, and another thread could be playing a video—all happening at the same time.
-Core: A part of the CPU that can handle tasks. If you have many cores, the computer can do more tasks at the same time.
-Multiple threads can run on one core (but they switch between each other), and they can run on multiple cores at the same time (if your computer has multiple cores).

-In python unless you explicitly use multiprocessing or threading, your program will run sequentially on a single core .
...........
Multithreading like having multiple "workers" inside one room (one process). These workers can work on different parts of the job, but they all share the same room (memory space).
Thread: A thread is a single task or unit of work within a program. Multiple threads can exist within a single process.
Threading: It is a way of making your program run multiple tasks at once (concurrently), but still within one process. These threads share the same memory and resources of the main process.

used for tasks that involve a lot of waiting and are I/O-bound eg: handling web requests, making API calls, or downloading files. 
.........
Multiprocessing is like having multiple separate rooms (processes) in which workers can perform tasks independently. 
Each room has its own resources (memory, etc.), and workers dont share the same space. Therefore, they can work completely independently.
Process: A process is a completely separate unit of work in your program. Each process has its own memory and resources.
Multiprocessing: When you use multiprocessing, you create multiple processes, each running its own code in its own memory space. Each process can run on a different CPU core, so tasks can be truly parallel.

used for tasks that require heavy computations and are CPU-bound eg;data processing, image manipulation, or running machine learning models.
'''




