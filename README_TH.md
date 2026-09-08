# การจำแนกรูปภาพสำหรับงานประกวดสุนัข

[English](README.md)

โปรเจกต์ Python เปรียบเทียบ **AlexNet**, **ResNet** และ **VGG** เพื่อแยกรูป
สุนัขออกจากรูปที่ไม่ใช่สุนัข และจำแนกสายพันธุ์สุนัข

## ภาพรวม

โปรเจกต์นี้จำลองการตรวจรูปสำหรับระบบลงทะเบียนงานประกวดสุนัข โดยใช้ CNN
ที่ผ่านการฝึกด้วย ImageNet มาแล้ว และเน้นการเขียนโปรแกรม Python เพื่อ:

1. รับค่าจาก command line
2. สร้าง label จริงจากชื่อไฟล์
3. จำแนกรูปด้วย CNN ที่เลือก
4. ตรวจว่า label จริงและผลทำนายเป็นสุนัขหรือไม่
5. คำนวณความแม่นยำและเวลา
6. เปรียบเทียบ AlexNet, ResNet และ VGG

โปรเจกต์นี้ไม่ได้ฝึก neural network ใหม่ แต่เป็นการนำ classifier ที่มีอยู่แล้ว
มาใช้งานผ่านกระบวนการที่เขียนด้วย Python

## ผลการทดสอบ

ชุดข้อมูลหลักมีรูปทั้งหมด 40 รูป แบ่งเป็นรูปสุนัข 30 รูปและรูปที่ไม่ใช่สุนัข
10 รูป

| โมเดล | สุนัขถูกต้อง | ไม่ใช่สุนัขถูกต้อง | สายพันธุ์ถูกต้อง | Label ตรงกัน | เวลา* |
|---|---:|---:|---:|---:|---:|
| ResNet | 100.0% | 90.0% | 90.0% | 82.5% | 5 วินาที |
| AlexNet | 100.0% | 100.0% | 80.0% | 75.0% | 2 วินาที |
| VGG | 100.0% | 100.0% | 93.3% | 87.5% | 19 วินาที |

\*เวลาอาจแตกต่างกันตามเครื่องและสภาพแวดล้อมที่ใช้รัน

**VGG เป็นโมเดลที่ดีที่สุดโดยรวม** เพราะแยก dog/not-dog ถูกต้อง 100% และ
จำแนกสายพันธุ์ได้แม่นยำที่สุดที่ 93.3% ส่วน AlexNet เป็นทางเลือกที่ดีเมื่อ
ให้ความสำคัญกับความเร็วมากกว่าความแม่นยำของสายพันธุ์

## วิธีใช้งาน

ติดตั้ง dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

รันด้วย VGG:

```bash
python3 check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

รันทั้งสามโมเดล:

```bash
sh run_models_batch.sh
```

รันกับรูปที่อัปโหลดเอง:

```bash
sh run_models_batch_uploaded.sh
```

ผลลัพธ์จะถูกบันทึกไว้ในโฟลเดอร์ `results/`

## สิ่งที่ได้เรียนรู้

- การใช้ `argparse` สร้าง command-line interface
- Dictionary, list, function และ mutable data
- การอ่านไฟล์และจัดรูปแบบ string
- การคำนวณ accuracy และเปอร์เซ็นต์
- การวัด runtime
- การเปรียบเทียบความแม่นยำกับ computational cost

## ที่มา

โปรเจกต์นี้จัดทำเป็นส่วนหนึ่งของหลักสูตร **AI Programming with Python** ของ
Udacity โดย starter code, classifier, mapping data และรูปชุดทดสอบมาจาก
[Udacity AIPND Revision](https://github.com/udacity/AIPND-revision)
