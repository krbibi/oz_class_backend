## 운영체제와 컴퓨터 하드웨어

### 1. CPU의 구성요소 ALU,CU 그리고 레지스터 각각의 역할을 간략하게 정리해보자

```
- ALU(Arithmetic and logical unit) : 산술논리연산자 연산담당파트 (산술:덧,뺄 / 논리 : and, or)
- CU(Control unit) : CPU에게 명령어가 전달되면 명령어를 해석
- 레지스터 : 데이터를 처리하기 위해 필요한 임시 저장장치
```

> 명령어가 전달되면 CU가 명령어를 해석하며 ALU에 결과를 보내어 연산을 수행하고 다음 명렁어는 레지스터에 임시 저장됨

### 2. 메인 메모리와 보조기억장치의 차이를 간략하게 서술해보자

```
- 메인 메모리(RAM) : 현재 실행되고 있는 프로그램의 명령어와 데이터를 저장 즉 프로그램이 실행되려면 반드시 메모리에 저장되어야 함
- 보조기억장치(HDD,SSD) : 워드,게임 같은 응용프로그램을 말함 사용자가 프로그램을 실행하면 프로세스가 되고 그때되서야 메인메모리로 가서 공간을 사용
```

### 3. 버스 시스템은 데이터를 주고받기위한 경로, 데이터의 종류에 따라 세가지로 구분되는데 그 세가지가 무엇인지

```
- 데이터버스 : 데이터 이동을 위해 필요한 버스
- 컨트롤버스 : cpu가 원하는 바를 메모리에 전달하기 위한 버스
- 어드레스버스 : 주소값을 이동하기 위해 필요한 버스
```

## 데드락

### 데드락이란?

```
프로세스가 자원을 얻지 못해 다음 처리를 하지 못하는 상태로 '교착상태' 라고도 하며 시스템적으로 한정된
자원을 여러 곳에서 사용하려고 할 때 발생합니다. 이 예시로 식사하는 철학자 문제 라는 것이 있습니다.
```

### 식사하는 철학자 문제

```
다섯 명의 철학자가 하나의 원탁에 앉아 식사를 한다. 각각의 철학자들 사이에는 포크가 하나씩 있고, 앞에는 접시가 있다.
접시 안에 든 요리는 포크를 두개 사용하여 먹어야만 한다. 그리고 각각의 철학자는 다른 철학자에게 말을 할 수 없으며,
번갈아가며 각자 식사하거나 생각하는 것만 가능하다. 따라서 식사를 하기 위해서는 왼쪽과 오른쪽의 인접한 철학자가
모두 식사를 하지 않고 생각하고 있어야만 한다. 또한 식사를 마치고 나면, 왼손과 오른손에 든 포크를 다른 철학자가
쓸 수 있도록 내려놓아야 한다. 이 때, 어떤 철학자도 굶지 않고 식사할 수 있도록 하는 방법은 무엇인가?
 출처 - [나무위키]
```

## 스레싱과 워킹셋

### 스레싱

```
특정 프로그램을 실행하기 위해 CPU가 메모리에 접근 하는데 페이지 부재(Page Fault)가 자주 발생하는 상황을 스레싱이라고 한다.
```

> 왜 스레싱이 발생할까?
> 컴퓨터에는 여러 프로그램이 동시에 메모리에 올라와있다. 즉 메모리에 올라와 있는 프로그램 개수에 맞게 한정된 메모리 자원을 나눠 가져야한다.
> 하지만, 프로그램마다 용량이 달라 빈부격차가 발생할 수 있다. 결국 운영체제가 특정 프로그램에 메모리를 너무 적게 할당할 때 발생한다.
> 출처 - [velog.io/jjuny7712.log]

```
프로세스의 처리시간보다 페이지 교체시간이 더 많아지는 현상
다중 프로그래밍의 정도가 높아짐에 따라 CPU의 이용률은 어느 특정 시점 까지는 올라가지만
다중 프로그래밍의 정도가 더욱 커지면 스레싱이 나타나고, CPU의 이용률은 급격히 감소된다.
 출처 - [https://chanyoung-dev.github.io/CS/OS/workingset/]
```

```
스레싱 해결 방법 : 워킹 셋 (Working set)
- 프로세스가 일정 시간 동안 자주 참조하는 페이지들의 집합
- 자주 참조되는 워킹 셋을 주기억장치에 상주시킴으로써 페이지 부재 및 페이지 교체 현상을 줄인다.
즉, 가장 많이 사용되는 페이지를 미리 저장하여 페이지 교체 현상을 해결함
```

## 연결리스트

### 연결리스트 자료구조에 대해

```
연결 리스트, 링크드 리스트(linked list)는 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는
방식으로 데이터를 저장하는 자료 구조이다. 이름에서 말하듯이 데이터를 담고 있는 노드들이 연결되어 있는데,
노드의 포인터가 다음이나 이전의 노드와의 연결을 담당하게 된다.
출처 - [위키백과]
```
