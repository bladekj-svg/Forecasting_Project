{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06b69eaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "from statsmodels.graphics.tsaplots import plot_acf, plot_pacf\n",
    "from statsmodels.stats.diagnostic import acorr_ljungbox\n",
    "\n",
    "\n",
    "\n",
    "def residual_diagnostics(residuals):\n",
    "\n",
    "    fig, axes = plt.subplots(2, 2, figsize=(10, 8))\n",
    "\n",
    "    residuals.plot(ax=axes[0, 0])\n",
    "    axes[0, 0].set_title('Residuals')\n",
    "\n",
    "    residuals.hist(ax=axes[0, 1])\n",
    "    axes[0, 1].set_title('Histogram')\n",
    "\n",
    "    plot_acf(residuals, ax=axes[1, 0])\n",
    "    plot_pacf(residuals, ax=axes[1, 1])\n",
    "\n",
    "    plt.tight_layout()\n",
    "\n",
    "    lb = acorr_ljungbox(residuals, lags=[10], return_df=True)\n",
    "\n",
    "    return fig, lb"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
