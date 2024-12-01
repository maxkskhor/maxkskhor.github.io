---
layout: post
title: "Concurrency in Python"
date: 2024-11-25 20:58:44 +0000
categories: python notes
permalink: /notes/python/concurrency
---

## Concurrency

1. Each Python interpreter is a process.
2. Python interpreter uses a single thread to run program. Additional Python threads can be started by a single interpreter.
3. Coroutine: a function that can suspend itself and resume later. Two types in Python:
   - Classic coroutine: generator function
   - Native coroutine: defined using **async def**
4. Python suspends the running thread every 5ms, making the GIL available to other pending threads.

### Asynchronous Programming

1. Keyword `await` is used to yield control back to the scheduler/event loop. It suspends the current coroutine.
2. Never use `time.sleep()` in `asyncio` coroutines as it will block the whole programme. Use `await asyncio.sleep()` - this yields control back to the event loop.
3. Only one coroutine is running at any time.

### Quotes

1. The `for` keyword works with _iterables_. The `await` keyword works with _awaitables_.
2. You rewrite all your code so none of it blocks or you're just wasting your time.
3. Concurrency: one of the most difficult topics in computer science (usually best avoided). - David Beazley
