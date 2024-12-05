import pandas as pd
import matplotlib.pyplot as plt

def process_and_plot_rain_data(input_csv):
    # Đọc file CSV
    data = pd.read_csv(input_csv)
    
    # Chuyển cột 'time' sang kiểu datetime
    data['time'] = pd.to_datetime(data['time'])
    
    # Thêm cột ngày và giờ để dễ dàng tổng hợp
    data['date'] = data['time'].dt.date
    data['hour'] = data['time'].dt.hour
    data['year'] = data['time'].dt.year
    
    # Lọc dữ liệu cho tháng 4 và tháng 10
    april_data = data[data['time'].dt.month == 4]
    october_data = data[data['time'].dt.month == 10]
    
    # Hàm tổng hợp dữ liệu
    def aggregate_data(month_data):
        # Bảng 1: Số lượng điểm ảnh mưa theo từng giờ trong các ngày
        rain_counts = (
            month_data[month_data['Status'] == 1]  # Chỉ lấy điểm ảnh mưa
            .groupby(['date', 'hour'])  # Nhóm theo ngày và giờ
            .size()
            .reset_index(name='Rain_Pixels')  # Đặt tên cho cột kết quả
        )
        
        # Bảng 2: Tổng lượng mưa theo từng giờ trong các ngày
        total_rain = (
            month_data.groupby(['date', 'hour'])['AWS']  # Nhóm theo ngày và giờ
            .sum()
            .reset_index(name='Total_Rainfall')  #
        )
        
        # Thêm cột 'datetime' để hỗ trợ vẽ biểu đồ
        rain_counts['datetime'] = pd.to_datetime(rain_counts['date'].astype(str) + ' ' + rain_counts['hour'].astype(str) + ':00')
        total_rain['datetime'] = pd.to_datetime(total_rain['date'].astype(str) + ' ' + total_rain['hour'].astype(str) + ':00')
        
        return rain_counts, total_rain
    
    april_rain_counts, april_total_rain = aggregate_data(april_data)
    october_rain_counts, october_total_rain = aggregate_data(october_data)

    # Vẽ biểu đồ
    def plot_monthly_data(rain_counts, total_rain, month_name):
        # Biểu đồ 1: Tổng số điểm mưa theo giờ
        plt.figure(figsize=(10, 6))
        plt.plot(rain_counts['datetime'], rain_counts['Rain_Pixels'], label='Tổng số điểm mưa', color='blue')
        plt.title(f'Tổng số điểm mưa theo giờ trong tháng {month_name}')
        plt.xlabel('Thời gian')
        plt.ylabel('Số lượng điểm mưa')
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()

        # Biểu đồ 2: Tổng lượng mưa theo giờ
        plt.figure(figsize=(10, 6))
        plt.plot(total_rain['datetime'], total_rain['Total_Rainfall'], label='Tổng lượng mưa (mm)', color='green')
        plt.title(f'Tổng lượng mưa theo giờ trong tháng {month_name}')
        plt.xlabel('Thời gian')
        plt.ylabel('Tổng lượng mưa (mm)')
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()

    # Biểu đồ cho từng năm
    def plot_yearly_data(rain_counts, total_rain, month_name):
        for year in rain_counts['datetime'].dt.year.unique():
            yearly_rain_counts = rain_counts[rain_counts['datetime'].dt.year == year]
            yearly_total_rain = total_rain[total_rain['datetime'].dt.year == year]

            # Biểu đồ: Tổng số điểm mưa theo giờ trong năm
            plt.figure(figsize=(10, 6))
            plt.plot(yearly_rain_counts['datetime'], yearly_rain_counts['Rain_Pixels'], label=f'Tổng số điểm mưa - {year}', color='blue')
            plt.title(f'Tổng số điểm mưa theo giờ trong tháng {month_name} - Năm {year}')
            plt.xlabel('Thời gian')
            plt.ylabel('Số lượng điểm mưa')
            plt.grid(True)
            plt.legend()
            plt.xticks(rotation=45)
            plt.show()

            # Biểu đồ: Tổng lượng mưa theo giờ trong năm
            plt.figure(figsize=(10, 6))
            plt.plot(yearly_total_rain['datetime'], yearly_total_rain['Total_Rainfall'], label=f'Tổng lượng mưa - {year}', color='green')
            plt.title(f'Tổng lượng mưa theo giờ trong tháng {month_name} - Năm {year}')
            plt.xlabel('Thời gian')
            plt.ylabel('Tổng lượng mưa (mm)')
            plt.grid(True)
            plt.legend()
            plt.xticks(rotation=45)
            plt.show()

    # Vẽ biểu đồ cho từng năm trong tháng 4
    plot_yearly_data(april_rain_counts, april_total_rain, "4")
    # Vẽ biểu đồ cho từng năm trong tháng 10
    plot_yearly_data(october_rain_counts, october_total_rain, "10")

# Gọi hàm với file đầu vào
process_and_plot_rain_data('FINAL_DATA.csv')
