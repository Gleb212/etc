function get_days(year, month)
		{
			let days = new Date(year, month, 32).getDate();

			return 32-days;
		}