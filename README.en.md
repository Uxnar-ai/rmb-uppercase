# rmb — digits to Chinese uppercase amounts

> Type an amount and get the Chinese uppercase form used on invoices and contracts, with the 元/角/分/整/零 rules handled. Dates can be written out the same way.

English | [中文](README.md)

## What it is

Invoices and remittance slips need 「壹万贰仟叁佰肆拾伍元陆角柒分」 written by hand, which is easy to get wrong and slow to count strokes for. This page encodes the rules.

The integer part is grouped in fours from the right; inside a group the digits take 仟/佰/拾/个, and groups are joined with 万/亿/万亿. Runs of zeros collapse to a single 零, trailing zeros inside a group are dropped, and 「一十五」 is not written as 「壹拾伍」. The fraction follows receipt convention: jiao without fen ends in 「壹角整」, fen without jiao is written 「零伍分」, whole yuan take 「整」, and amounts below one yuan are prefixed with 「零元」.

The date block offers both styles: Chinese characters (二零二六年十月三十一日, common in official documents) and digit-by-digit uppercase (贰零贰陆年壹拾月叁拾壹日, for receipts). The amount algorithm passed 16 edge cases in node (0, 0.05, 0.56, 1005, one hundred million and one, the largest value before 万亿) before going live.

## Features

- Amount to Chinese uppercase with all the 元/角/分/整/零 conventions
- Up to 万亿 with two decimals
- Also shows the plain digits, thousands separators and spoken reading, each copyable
- Dates written in Chinese characters
- Dates written digit-by-digit in uppercase
- Five quick amount presets
- Auto light/dark plus manual toggle

## Stack

Python 3.12 · Flask 3.1 · 原生 JS

## Run

```bash
pip install -r requirements.txt
python app.py  # 默认 127.0.0.1:8883
```

## About

Part of the **auto-lab** series — small projects written, deployed and maintained automatically by [Nix](https://github.com/Uxnar-ai) on a self-hosted server.

Placeholders such as `<SERVER_IP>` and `<LOCAL_PATH>` are sanitised values applied at publish time. This repository contains no credentials, internal addresses or personal data.

## License

MIT
