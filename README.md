# Picture_cutting
训练示例图裁剪并制作PDF

# 效果
![94297d1dae827a81bc0b9763516786ca](https://github.com/user-attachments/assets/2b9accc5-8ac8-408f-b78e-999481930cd3)
![8845140db63210f042aa453d4e613308](https://github.com/user-attachments/assets/74dd1363-d937-436b-a9bc-291594aac258)



# 安装

测试环境python3.12.4

```
git clone https://github.com/fallingmeteorite/Picture_cutting.git

cd Picture_cutting

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

mkdir Images_save

mkdir Pretreatment
```
# 准备
Pretreatment文件夹存放要处理图片

# 运行

```
python run.py 
```

# 可修改参数
run.py文件中函数导入值
width_incise=3, 宽平分个数
height_incise=5, 长平分个数
quality_save=10, 保存图片质量
