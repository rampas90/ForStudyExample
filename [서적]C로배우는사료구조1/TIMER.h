#pragma once
#ifndef _TIMER_H
#define _TIMER_H

#pragma comment(lib, "winmm.lib")

#include <windows.h> 

#define get_tick() (long)timeGetTime()
#define diff_tick(t1,t2)  (long)(t2-t1)
#define diff_second(t1,t2) (float)((t2-t1)* 0.001f); 

#endif