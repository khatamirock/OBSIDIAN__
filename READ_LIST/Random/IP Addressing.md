# 🧮 1. Example Question (Exam Type)

**Q:**  
Given the IP address **192.168.10.18/26**, find —

1. The **subnet mask**
    
2. The **network address**
    
3. The **broadcast address**
    
4. The **range of valid hosts**
    
5. The **number of hosts** per subnet
    

---

## 🧠 Step-by-Step Intuitive Solution

### 1️⃣ CIDR → Subnet Mask

`/26` means **26 bits** are for the network portion.  
👉 The subnet mask in binary:

```
11111111.11111111.11111111.11000000
```

Convert to decimal:

```
255.255.255.192
```

✅ **Subnet Mask = 255.255.255.192**

---

### 2️⃣ Find Subnet Size

The **last octet** has `2` host bits (since 32 - 26 = 6 host bits).  
So each subnet has block size of:

```
256 - 192 = 64
```

So subnets are:

```
192.168.10.0
192.168.10.64
192.168.10.128
192.168.10.192
```

---

### 3️⃣ Find Network Address

We apply the **bitwise AND** between:

```C
IP address     192.168.10.18  →  11000000.10101000.00001010.00010010 
Subnet mask    255.255.255.192 → 11111111.11111111.11111111.11000000
```

==AND== them:

```
Result → 11000000.10101000.00001010.00000000
````

Convert back to decimal:

`192.168.10.0`

✅ **Network address = 192.168.10.0**

---

### 4️⃣ Find Broadcast Address

Each subnet has 64 addresses.  
So the broadcast is 1 less than next subnet’s start:

`192.168.10.63`

✅ **Broadcast Address = 192.168.10.63**

---

### 5️⃣ Valid Host Range

Hosts lie between network and broadcast:

```
192.168.10.1 → 192.168.10.62
```

✅ **Valid Host Range = 192.168.10.1 – 192.168.10.62**

---

### 6️⃣ Number of Hosts

Formula:

```
2^(32 – subnet bits) – 2
= 2^(32 – 26) – 2
= 2^6 – 2 = 62
```

✅ **62 hosts per subnet**

---

## ✨ Final Answers

|Property|Value|
|---|---|
|IP|192.168.10.18/26|
|Subnet Mask|255.255.255.192|
|Network Address|192.168.10.0|
|Broadcast Address|192.168.10.63|
|Valid Host Range|192.168.10.1 – 192.168.10.62|
|Hosts per Subnet|62|

---


# 🧩 2. Example 2:

**Given IP:** 172.16.35.123/20  
Find —

1. Subnet mask
    
2. Network address
    
3. Broadcast address
    
4. Valid host range
    
5. Number of hosts
    

---

## 🧠 Step-by-Step Intuitive Solution

### 1️⃣ CIDR → Subnet Mask

`/20` means first **20 bits** for network, rest **12 bits** for host.

So in binary:

```
11111111.11111111.11110000.00000000
```

Convert to decimal →  
✅ **Subnet Mask = 255.255.240.0**

---

### 2️⃣ Block Size

The **interesting part** (changing part) is in the **third octet**, because that’s where the mask stops (`/20` → 8 + 8 + 4 bits used).

So block size =

```
256 - 240 = 16
```

So subnets in the 3rd octet go like:

```
172.16.0.0
172.16.16.0
172.16.32.0
172.16.48.0
172.16.64.0
... and so on
```

---

### 3️⃣ Find Network Address

Now check where **172.16.35.123** fits.

Look at the **third octet = 35**  
→ 35 lies between **32 and 48**

✅ Therefore, **Network Address = 172.16.32.0**

```
11111111.11111111.11110000.00000000
172.16           .00100011.01111011

172.16.          .00100000.00000000   /20
					32
```


---

### 4️⃣ Find Broadcast Address

``` C
Network bits (20) | Host bits (12)
10101100.00010000.0010|0011.01111011
```


Octet	Binary	Decimal
1st	10101100	172
2nd	00010000	16
3rd	0010.1111	47
4th	11111111	255

---

### 5️⃣ Valid Host Range

## ⚙️ Step 4. Host Range

Between Network and Broadcast:

- **Network**: 172.16.32.0
- **First Host**: 172.16.32.1
- **Last Host**: 172.16.47.254
- **Broadcast**: 172.16.47.255

✅ **Host range = 172.16.32.1 – 172.16.47.254**

| 3rd Octet | Binary | Meaning       |
| --------- | ------ | ------------- |
| 00100000  | 32     | Network start |
| 00101111  | 47     | Broadcast     |

---

### 6️⃣ Number of Hosts

Formula:

```
2^(32 – 20) – 2 = 2^12 – 2 = 4094
```

✅ **Hosts per subnet = 4094**

---

## ✨ Final Answers

|Property|Value|
|---|---|
|IP|172.16.35.123/20|
|Subnet Mask|255.255.240.0|
|Network Address|172.16.32.0|
|Broadcast Address|172.16.47.255|
|Valid Host Range|172.16.32.1 – 172.16.47.254|
|Hosts per Subnet|4094|

🧩 Summary

| Item        | Binary                              | Decimal                     |
| ----------- | ----------------------------------- | --------------------------- |
| IP Address  | 10101100.00010000.00100011.01111011 | 172.16.35.123               |
| Subnet Mask | 11111111.11111111.11110000.00000000 | 255.255.240.0               |
| Network     | 10101100.00010000.00100000.00000000 | 172.16.32.0                 |
| Broadcast   | 10101100.00010000.00101111.11111111 | 172.16.47.255               |
| Host range  | —                                   | 172.16.32.1 → 172.16.47.254 |


---
# VLSM:

## Problem (exam-style)

You have network **192.168.1.0/24**. Create subnets (VLSM) for these departments with the **minimum** waste:

- Sales — **100 hosts**
    
- HR — **60 hosts**
    
- IT — **30 hosts**
    
- GuestWiFi — **12 hosts**
    
- CCTV — **6 hosts**
    
- Admin — **2 hosts**
    

Sort requirements by size and allocate from the start of the /24 (left-to-right).

---

### Method (what you must show in exam)

1. **Sort** requirements descending by required hosts.
    
2. For each requirement, find the **smallest subnet** that fits: need `required + 2` addresses (network + broadcast).
    
    - Find smallest power-of-two block `2^h >= required+2` where `h` = number of host bits.
        
    - Prefix = `32 - h`. Netmask from the prefix.
        
3. **Allocate** that block at the next available address (no overlap).
    
4. Repeat until done.
    

I did that; here’s the allocation.

---

### Allocation result (final table)

|Dept|Req hosts|Prefix|Netmask|Network|First host|Last host|Broadcast|Usable hosts|
|---|--:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Sales|100|/25|255.255.255.128|**192.168.1.0**|192.168.1.1|192.168.1.126|192.168.1.127|126|
|HR|60|/26|255.255.255.192|**192.168.1.128**|192.168.1.129|192.168.1.190|192.168.1.191|62|
|IT|30|/27|255.255.255.224|**192.168.1.192**|192.168.1.193|192.168.1.222|192.168.1.223|30|
|GuestWiFi|12|/28|255.255.255.240|**192.168.1.224**|192.168.1.225|192.168.1.238|192.168.1.239|14|
|CCTV|6|/29|255.255.255.248|**192.168.1.240**|192.168.1.241|192.168.1.246|192.168.1.247|6|
|Admin|2|/30|255.255.255.252|**192.168.1.248**|192.168.1.249|192.168.1.250|192.168.1.251|2|

> Remaining addresses in the /24 after these allocations: **192.168.1.252 – 192.168.1.255** (4 addresses — typically reserved or used for tiny links, /30, or future growth).

---

### How those prefixes were chosen (quick logic — show work)

For each required host count `H`:

- Compute `need = H + 2`.
    
- Find smallest `h` such that `2^h >= need`.
    
- Prefix = `32 - h`.  
    Examples from the table:
    
- Sales 100 → need = 102 → smallest power `2^7 = 128` so `h=7` → prefix = `32-7 = /25` → usable hosts `128-2 = 126`.
    
- HR 60 → need = 62 → `2^6 = 64` so `/26` → usable `62`.
    
- IT 30 → need = 32 → `2^5 = 32` so `/27` → usable `30`.
    
- GuestWiFi 12 → need = 14 → `2^4 = 16` so `/28` → usable `14`.
    
- CCTV 6 → need = 8 → `2^3 = 8` so `/29` → usable `6`.
    
- Admin 2 → need = 4 → `2^2 = 4` so `/30` → usable `2`.
    

This is the exact method graders expect.

---

### Bit-level quick check (example: Sales /25)

Sales got `192.168.1.0/25`. In binary:

- Network: `192.168.1.0` → `11000000.10101000.00000001.00000000`
    
- Prefix `/25` → mask `11111111.11111111.11111111.10000000` (netmask 255.255.255.128)
    
- Host bits = 7 bits → range for last octet `00000000` → `01111111` → 0..127
    
- Usable hosts = 1..126 (`00000001` → `01111110`)
    

That matches table entries (first host .1 last host .126, broadcast .127).

---

