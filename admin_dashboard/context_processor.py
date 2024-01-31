from admin_dashboard.models import SiteInfoModel


def site_info(request):
    info = SiteInfoModel.objects.first()

    return {
        'site_info': info
    }
