import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# LOAD DATASET
# =====================================================

file_path = "sales_data_sample.xlsx"

df = pd.read_excel(file_path)

# =====================================================
# CLEAN COLUMN NAMES
# =====================================================

df.columns = df.columns.str.lower().str.replace(' ', '_')

# =====================================================
# HANDLE MISSING VALUES
# =====================================================

for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# =====================================================
# CREATE CLEAN PROFESSIONAL DASHBOARD
# =====================================================

fig, axes = plt.subplots(2, 3, figsize=(22, 12))

fig.suptitle(
    "SMART BUSINESS ANALYTICS DASHBOARD",
    fontsize=26,
    fontweight='bold'
)

# =====================================================
# GRAPH 1 : MONTHLY SALES TREND
# =====================================================

monthly_sales = df.groupby('month_id')['sales'].sum()

axes[0,0].plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o',
    linewidth=3
)

axes[0,0].set_title(
    "Monthly Sales Trend",
    fontsize=16
)

axes[0,0].set_xlabel("Month")
axes[0,0].set_ylabel("Sales")

# =====================================================
# GRAPH 2 : PRODUCT LINE SALES
# =====================================================

product_sales = (
    df.groupby('productline')['sales']
    .sum()
    .sort_values(ascending=False)
)

axes[0,1].bar(
    product_sales.index,
    product_sales.values
)

axes[0,1].set_title(
    "Product Line Sales",
    fontsize=16
)

axes[0,1].tick_params(
    axis='x',
    rotation=25
)

# =====================================================
# GRAPH 3 : TOP 5 COUNTRY SALES
# =====================================================

country_sales = (
    df.groupby('country')['sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

axes[0,2].pie(
    country_sales.values,
    labels=country_sales.index,
    autopct='%1.1f%%'
)

axes[0,2].set_title(
    "Top Country Sales",
    fontsize=16
)

# =====================================================
# GRAPH 4 : ORDER STATUS
# =====================================================

status_counts = df['status'].value_counts()

axes[1,0].bar(
    status_counts.index,
    status_counts.values
)

axes[1,0].set_title(
    "Order Status Analysis",
    fontsize=16
)

axes[1,0].tick_params(
    axis='x',
    rotation=25
)

# =====================================================
# GRAPH 5 : SALES DISTRIBUTION
# =====================================================

axes[1,1].hist(
    df['sales'],
    bins=20
)

axes[1,1].set_title(
    "Sales Distribution",
    fontsize=16
)

axes[1,1].set_xlabel("Sales")

# =====================================================
# GRAPH 6 : CORRELATION HEATMAP
# =====================================================

numeric_df = df.select_dtypes(include='number')

sns.heatmap(
    numeric_df.corr(),
    ax=axes[1,2],
    cmap='coolwarm',
    annot=True,
    fmt=".1f"
)

axes[1,2].set_title(
    "Correlation Heatmap",
    fontsize=16
)

# =====================================================
# GIVE PERFECT SPACING
# =====================================================

plt.subplots_adjust(
    top=0.88,
    bottom=0.08,
    left=0.05,
    right=0.97,
    hspace=0.45,
    wspace=0.30
)

# =====================================================
# FULL SCREEN WINDOW
# =====================================================

manager = plt.get_current_fig_manager()

manager.window.state('zoomed')

# =====================================================
# SHOW DASHBOARD
# =====================================================

plt.show()