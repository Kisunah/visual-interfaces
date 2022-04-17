from bs4 import BeautifulSoup
import requests as req
import csv
import os

episodeDoc = """

<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>Category:Transcripts | Superstore Wiki | Fandom</title>
<script>document.documentElement.className = document.documentElement.className.replace( /(^|\s)client-nojs(\s|$)/, "$1client-js$2" );</script>
<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgCanonicalNamespace":"Category","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":14,"wgPageName":"Category:Transcripts","wgTitle":"Transcripts","wgCurRevisionId":23982,"wgRevisionId":23982,"wgArticleId":3101,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":[],"wgBreakFrames":false,"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgRelevantPageName":"Category:Transcripts","wgRelevantArticleId":3101,"wgRequestId":"4241f5d39b9a2150","wgCSPNonce":false,"wgIsProbablyEditable":false,"wgRelevantPageIsProbablyEditable":false,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgNoExternals":false,"wgArticleInterlangList":[],"wikiaPageType":"article","isDarkTheme":false,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en","usePageImages":true,"usePageDescriptions":false},"wgEnableLightboxExt":true,"wgPopupsReferencePreviews":true,"wgPopupsShouldSendModuleToUser":true,"wgPopupsConflictsWithNavPopupGadget":false,"wgEnablePopups":false,"wgIsTestWiki":false,"wgMFDisplayWikibaseDescriptions":{"search":false,"nearby":false,"watchlist":false,"tagline":false},"egMapsScriptPath":"/extensions/Maps/","egMapsDebugJS":false,"egMapsAvailableServices":["leaflet","googlemaps3"],"egMapsLeafletLayersApiKeys":{"MapBox":"","MapQuestOpen":"","Thunderforest":"","GeoportailFrance":""},"wgVisualEditorToolbarScrollOffset":0,"wgVisualEditorUnsupportedEditParams":["undo","undoafter","veswitched"],"wgEditSubmitButtonLabelPublish":false,"wgCodeMirrorEnabled":true,"egFacebookAppId":"112328095453510","comscoreKeyword":"wikiacsid_tv","quantcastLabels":"Genre.live-action,Genre.comedy,Genre.drama,Genre.romance,Media.tv,Media.music,TV.nbc,Theme.sliceoflife","wgCategorySelect":{"defaultNamespace":"Category","defaultNamespaces":"Category"},"wgEnableDiscussions":true,"viewTrackURL":"https://beacon.wikia-services.com/__track/view?a=3101\u0026n=14\u0026env=prod\u0026c=1298936\u0026lc=en\u0026lid=75\u0026x=superstorenbc\u0026s=ucp_desktop\u0026mobile_theme=fandom-light\u0026rollout_tracking=ucp","viewTrackUrlPrefix":"https://beacon.wikia-services.com/__track/view?a=3101\u0026n=14\u0026env=prod\u0026c=1298936\u0026lc=en\u0026lid=75\u0026x=superstorenbc\u0026s=ucp_desktop\u0026mobile_theme=fandom-light\u0026rollout_tracking=ucp","wgEnableHydraFeatures":false,"wgEnableWikiaBarExt":true,"wgEnableWikiaBarAds":true,"wgWikiaBarMainLanguages":["de","en","es","fr"],"wgPageLanguageHasWordBreaks":true,"wgPerformanceMonitoringSamplingFactor":10,"wgPerformanceMonitoringEndpointUrl":"https://beacon.wikia-services.com/__track/special/performance_metrics?w=1298936\u0026lc=en\u0026d=superstorenbc\u0026s=ucp_desktop\u0026u=0\u0026i=sjc-prod\u0026a=https%3A%2F%2Fsuperstore-nbc.fandom.com%2Fwiki%2FCategory%3ATranscripts","wgSoftwareVersion":"release-360.042_release-381.001@release-360.042_release-381.001","isGamepedia":false,"wgRailModuleList":["Fandom\\FandomDesktop\\Rail\\PopularPagesModuleService"],"wgRailModuleParams":[]});mw.loader.state({"site.styles":"ready","noscript":"ready","user.styles":"ready","site":"ready","user.options":"ready","user.tokens":"loading","ext.fandom.CategoryPage.category-layout-selector.css":"ready","ext.fandom.CategoryPage.category-page3.css":"ready","mediawiki.legacy.shared":"ready","mediawiki.legacy.commonPrint":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.staffSig.css":"ready","vendor.bootstrap.popover.css":"ready","ext.fandom.bannerNotifications.desktop.css":"ready","ext.fandom.quickBar.css":"ready","ext.fandom.UserPreferencesV2.css":"ready","ext.fandom.CreatePage.css":"ready","ext.fandom.Thumbnails.css":"ready","ext.fandom.FandomEmbedVideo.css":"ready","ext.fandom.ArticleInterlang.css":"ready","ext.fandom.SearchExperiment.css":"ready","ext.fandom.HighlightToAction.css":"ready","ext.tmh.thumbnail.styles":"ready","skin.fandomdesktop.css":"ready","ext.fandomVideo.css":"ready","ext.fandom.GlobalComponents.GlobalComponentsTheme.nav-default.css":"ready","ext.fandom.GlobalComponents.GlobalComponentsTheme.light.css":"ready","ext.fandom.GlobalComponents.GlobalNavigation.css":"ready","ext.fandom.GlobalComponents.GlobalFooter.css":"ready","ext.fandom.GlobalComponents.CommunityHeader.css":"ready","ext.fandom.GlobalComponents.StickyNavigation.css":"ready","ext.fandom.GlobalComponents.CommunityHeaderBackground.css":"ready","skin.fandomdesktop.rail.popularPages.css":"ready","skin.fandomdesktop.rail.css":"ready"});mw.loader.implement("user.tokens@0tffind",function($,jQuery,require,module){/*@nomin*/mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
});RLPAGEMODULES=["ext.fandom.CategoryPage.CategoryLayoutSelector.js","mediawiki.page.startup","mediawiki.page.ready","mediawiki.searchSuggest","ext.fandom.mediaWikiMigrationHooks.js","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.fandom.FacebookTags.js","ext.fandom.ae.babTracking.js","ext.fandom.ae.consentQueue.js","ext.fandom.AnalyticsEngine.comscore.js","ext.fandom.AnalyticsEngine.quantcast.js","ext.categorySelect.js","ext.categorySelectFandomDesktop.css","ext.fandom.bannerNotifications.js","ext.fandom.HeartbeatTracking.js","ext.fandom.Track.pageview.js","ext.fandom.wikiaBar.js","ext.fandom.ContentReview.legacyLoaders.js","ext.fandom.ContentReview.jsReload.js","ext.fandom.ImportJs","ext.fandom.UncrawlableUrl.anchors.js","ext.fandom.CreatePage.js","ext.fandom.TimeAgoMessaging.js","ext.fandom.VisitSource.js","ext.fandom.Thumbnails.js","ext.popups","ext.fandom.FandomEmbedVideo.js","ext.fandom.WikiaInYourLang.js","ext.fandom.performanceMonitoring.js","ext.fandom.SearchExperiment.js","ext.fandom.HighlightToAction.js","mw.MediaWikiPlayer.loader","mw.PopUpMediaTransform","skin.fandomdesktop.js","skin.fandomdesktop.messages","ext.fandom.GlobalComponents.GlobalNavigation.js","ext.fandom.GlobalComponents.Notifications.messages","ext.fandom.GlobalComponents.SearchModal.messages","ext.fandom.GlobalComponents.GlobalFooter.js","ext.fandom.GlobalComponents.CommunityHeader.js","ext.fandom.GlobalComponents.StickyNavigation.js","skin.fandomdesktop.rail.toggle.js","skin.fandomdesktop.rail.lazyRail.js","ext.fandom.Lightbox.js"];mw.loader.load(RLPAGEMODULES);});</script>
<link rel="stylesheet" href="/load.php?fandomdesktop=1&amp;lang=en&amp;modules=ext.fandom.ArticleInterlang.css%7Cext.fandom.CategoryPage.category-layout-selector.css%7Cext.fandom.CategoryPage.category-page3.css%7Cext.fandom.CreatePage.css%7Cext.fandom.FandomEmbedVideo.css%7Cext.fandom.GlobalComponents.CommunityHeader.css%7Cext.fandom.GlobalComponents.CommunityHeaderBackground.css%7Cext.fandom.GlobalComponents.GlobalComponentsTheme.light.css%7Cext.fandom.GlobalComponents.GlobalComponentsTheme.nav-default.css%7Cext.fandom.GlobalComponents.GlobalFooter.css%7Cext.fandom.GlobalComponents.GlobalNavigation.css%7Cext.fandom.GlobalComponents.StickyNavigation.css%7Cext.fandom.HighlightToAction.css%7Cext.fandom.SearchExperiment.css%7Cext.fandom.Thumbnails.css%7Cext.fandom.UserPreferencesV2.css%7Cext.fandom.bannerNotifications.desktop.css%7Cext.fandom.quickBar.css%7Cext.fandomVideo.css%7Cext.staffSig.css%7Cext.tmh.thumbnail.styles%7Cext.visualEditor.desktopArticleTarget.noscript%7Cmediawiki.legacy.commonPrint%2Cshared%7Cskin.fandomdesktop.css%7Cskin.fandomdesktop.rail.css%7Cskin.fandomdesktop.rail.popularPages.css%7Cvendor.bootstrap.popover.css&amp;only=styles&amp;skin=fandomdesktop"/>
<script async="" src="/load.php?cb=20201124072642&amp;fandomdesktop=1&amp;lang=en&amp;modules=startup&amp;only=scripts&amp;skin=fandomdesktop"></script>
<meta name="ResourceLoaderDynamicStyles" content=""/>
<link rel="stylesheet" href="/load.php?fandomdesktop=1&amp;lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=fandomdesktop"/>
<meta name="generator" content="MediaWiki 1.33.3"/>
<meta name="twitter:card" content="summary"/>
<meta name="twitter:site" content="@getfandom"/>
<meta name="twitter:url" content="https://superstore-nbc.fandom.com/wiki/Category:Transcripts"/>
<meta name="twitter:title" content="Category:Transcripts | Superstore Wiki | Fandom"/>
<meta name="twitter:description" content="A directory of episode transcripts."/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes, minimum-scale=0.25, maximum-scale=5.0"/>
<link href="/wikia.php?controller=ThemeApi&amp;method=themeVariables&amp;cityId=1298936&amp;version=1649781088" rel="stylesheet"/>
<link rel="shortcut icon" href="https://static.wikia.nocookie.net/superstore-nbc/images/4/4a/Site-favicon.ico/revision/latest?cb=20210714141106"/>
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch_desc.php" title="Superstore Wiki (en)"/>
<link rel="EditURI" type="application/rsd+xml" href="https://superstore-nbc.fandom.com/api.php?action=rsd"/>
<link rel="license" href="https://www.fandom.com/licensing"/>
<link rel="canonical" href="https://superstore-nbc.fandom.com/wiki/Category:Transcripts"/>
	<meta property="fb:app_id" content="112328095453510" prefix="fb: http://www.facebook.com/2008/fbml"/>

	<meta property="og:type" content="article"/>

	<meta property="og:site_name" content="Superstore Wiki"/>

	<meta property="og:title" content="Transcripts"/>

	<meta property="og:url" content="https://superstore-nbc.fandom.com/wiki/Category:Transcripts"/>

	<meta property="og:image" content="https://static.wikia.nocookie.net/ucp-internal-test-starter-commons/images/a/aa/FandomFireLogo.png/revision/latest/zoom-crop/width/200/height/200?cb=20210713142711"/>

<script>var _plc={"p":"mw","pVar":"fandomdesktop","pCat":"tv","pId":"1298936","pg":"article","pgId":"3101","pgLang":"en","adTags":{"tv":["nbc"],"sex":["f","m"],"theme":["sliceoflife"],"gnre":["drama","live-action","sitcom","comedy","romance"],"media":["music","tv"],"age":["25-34","18-24"]},"time":0}; var _ulc={"id":"0","lang":"en"}; _plc.time=Date.now();</script>
<script src="https://static.wikia.nocookie.net/silversurfer/prod/latest/sdk.js" defer=""></script>
<script src="https://static.wikia.nocookie.net/silversurfer/prod/latest/pathfinder.js" defer=""></script>
<script>var ads={"context":{"opts":{"enableNativeAds":true,"enableAdTagManagerBackend":true,"pageType":"all_ads","platformName":"fandomdesktop"},"targeting":{"enablePageCategories":true,"esrbRating":"teen","isUcp":true,"mappedVerticalName":"ent","newWikiCategories":["ent"],"pageArticleId":3101,"pageIsArticle":true,"pageName":"Category:Transcripts","pageType":"article","wikiCustomKeyValues":"sex=m;sex=f;gnre=live-action;gnre=comedy;gnre=drama;gnre=romance;media=tv;media=music;tv=nbc;theme=sliceoflife","wikiDbName":"superstorenbc","wikiId":1298936,"wikiLanguage":"en","wikiVertical":"tv","adTagManagerTags":{"tv":["nbc"],"sex":["f","m"],"theme":["sliceoflife"],"gnre":["drama","live-action","sitcom","comedy","romance"],"media":["music","tv"],"age":["25-34","18-24"]}}},"consentQueue":[]};</script>
<script>
	// Install temporary stub until full CMP will be ready
	if (typeof window.__tcfapi === 'undefined') {
		// @iabtcf/stub v1.3.1
		"use strict";function _typeof(t){return(_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t})(t)}!function(){var t=function(){var t,e,o="__tcfapiLocator",n=[],r=window,a=r;for(;a;){try{if(a.frames[o]){t=a;break}}catch(t){}if(a===r.top)break;a=r.parent}t||(!function t(){var e=r.document,n=!!r.frames[o];if(!n)if(e.body){var a=e.createElement("iframe");a.style.cssText="display:none",a.name=o,e.body.appendChild(a)}else setTimeout(t,5);return!n}(),r.__tcfapi=function(){for(var t=arguments.length,o=new Array(t),r=0;r<t;r++)o[r]=arguments[r];if(!o.length)return n;"setGdprApplies"===o[0]?o.length>3&&2===parseInt(o[1],10)&&"boolean"==typeof o[3]&&(e=o[3],"function"==typeof o[2]&&o[2]("set",!0)):"ping"===o[0]?"function"==typeof o[2]&&o[2]({gdprApplies:e,cmpLoaded:!1,cmpStatus:"stub"}):n.push(o)},r.addEventListener("message",(function(t){var e="string"==typeof t.data,o={};if(e)try{o=JSON.parse(t.data)}catch(t){}else o=t.data;var n="object"===_typeof(o)?o.__tcfapiCall:null;n&&window.__tcfapi(n.command,n.version,(function(o,r){var a={__tcfapiReturn:{returnValue:o,success:r,callId:n.callId}};t&&t.source&&t.source.postMessage&&t.source.postMessage(e?JSON.stringify(a):a,"*")}),n.parameter)}),!1))};"undefined"!=typeof module?module.exports=t:t()}();
	}
</script>

<script src="https://services.fandom.com/icbm/api/loader?app=fandomdesktop" defer=""></script>
<script>
	window.RLQ = window.RLQ || [];
	window.RLQ.push(function() {
		function genUID() {
			return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
				const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
				return v.toString(16);
			});
		}
		function getCookie(cookieName) {
			const cookieSplit = ('; ' + document.cookie).split('; ' + cookieName + '=');
			return cookieSplit.length === 2 ? cookieSplit.pop().split(';').shift() : null;
		}
		mw.config.set({
			sessionId: getCookie('tracking_session_id') || genUID(),
			pvNumber: (parseInt(getCookie('pv_number'), 10) || 0) + 1,
			pvNumberGlobal: (parseInt(getCookie('pv_number_global'), 10) || 0) + 1,
			pvUID: genUID()
		});
	});
</script>


<script>
	const useMaxDefaultContentWidth = Boolean();

	const defaultContentWidth = useMaxDefaultContentWidth ? 'expanded' : 'collapsed';
	const contentWidthPreference = localStorage.getItem('contentwidth') || defaultContentWidth;

	if ( contentWidthPreference === 'expanded' ) {
		document.documentElement.classList.add('is-content-expanded');
	}
</script>

<script>
	(function trackFCPPageView(config) {
		let beacon;
		let sessionId;
		let pvNumber;
		let pvNumberGlobal;

		function readCookies() {
			beacon = getCookieValue('wikia_beacon_id');
			sessionId = getCookieValue('tracking_session_id') || genUID();
			pvNumber = getCookieValue('pv_number') || 0;
			pvNumberGlobal = getCookieValue('pv_number_global') || 0;
		}

		function getCookieValue(cookieName) {
			const cookieSplit = ('; ' + document.cookie).split('; ' + cookieName + '=');

			return cookieSplit.length === 2 ? cookieSplit.pop().split(';').shift() : null;
		}

		function genUID() {
			return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
				const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);

				return v.toString(16);
			});
		}

		function getEventParams() {
			let computedPVNumber = pvNumber ? parseInt(pvNumber, 10) : 0;
			let computedPVNumberGlobal = pvNumberGlobal ? parseInt(pvNumberGlobal, 10) : 0;

			if (!window.fandomTrackingCookiesSet) {
				computedPVNumber += 1;
				computedPVNumberGlobal += 1;
			}

			const params = {
				beacon: beacon,
				cb: new Date().valueOf(),
				session_id: sessionId,
				pv_unique_id: genUID(),
				pv_number: computedPVNumber,
				pv_number_global: computedPVNumberGlobal,
				url: window.location.href,
				c: config.wgCityId,
				a: config.wgArticleId,
				lc: config.wgContentLanguage,
				x: config.wgDBname,
				s: (
					config.skin === 'fandommobile' ? 'ucp_mobile' :
					config.skin === 'fandomdesktop' ? 'ucp_desktop' :
					config.skin
				),
				n: config.wgNamespaceNumber,
			};

			if (document.referrer) {
				params.r = encodeURIComponent(document.referrer);
			}

			return params;
		}

		function setCookies() {
			if (!getCookieValue('tracking_session_id')) {
				const expireDate = new Date(Date.now() + 1000 * 60 * 30);

				document.cookie = 'tracking_session_id=' + sessionId + '; expires=' + expireDate.toGMTString() +
					';domain=' + config.wgCookieDomain + '; path=' + config.wgCookiePath + ';';
			}
		}

		function track() {
			const requestUrl = 'https://beacon.wikia-services.com/__track/special/fcp_pageview';

			readCookies();
			setCookies();

			const params = getEventParams();
			const queryParams = Object.keys(params)
					.map((key) => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
					.join('&');

			fetch(`${requestUrl}?${queryParams}`, { mode: 'no-cors', keepalive: true });
		}

		requestAnimationFrame(() => {
			requestAnimationFrame(() => {
				window.ads.consentQueue = window.ads.consentQueue || [];
				window.ads.consentQueue.push(function (consents) {
					if( consents.gdprConsent === true ) {
						track();
					}
				});
			})
		})
	})({"wgCookieDomain":".fandom.com","wgCookiePath":"\/","wgScriptPath":"","wgCityId":1298936,"wgDBname":"superstorenbc","wgArticleId":3101,"wgContentLanguage":"en","wgNamespaceNumber":14,"skin":"fandomdesktop"});
</script>

<!--[if lt IE 9]><script src="/load.php?fandomdesktop=1&amp;lang=en&amp;modules=html5shiv&amp;only=scripts&amp;skin=fandomdesktop&amp;sync=1"></script><![endif]-->
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-14 ns-subject page-Category_Transcripts rootpage-Category_Transcripts skin-fandomdesktop action-view ooui-theme-fandomooui wiki-superstorenbc theme-fandomdesktop-light">
<div class="notifications-placeholder">
		<div class="banner-notifications-placeholder">
		<div class="wds-banner-notification__container">
	
</div>
	</div>
</div>
<div class="fandom-sticky-header">
		<a href="//superstore-nbc.fandom.com" class="fandom-sticky-header__sitename">Superstore Wiki</a>
	
<nav class="fandom-community-header__local-navigation">
	<ul class="wds-tabs">
					
			<li class="wds-dropdown explore-menu">
			<div class="wds-tabs__tab-label wds-dropdown__toggle first-level-item">
				<a href="#"
				   data-tracking="custom-level-1"
									>
					<svg class="wds-icon-tiny wds-icon"><use xlink:href="#wds-icons-book-tiny"></use></svg>					<span>Explore</span>
				</a>
				<svg class="wds-icon wds-icon-tiny wds-dropdown__toggle-chevron"><use xlink:href="#wds-icons-dropdown-tiny"></use></svg>			</div>
			<div class="wds-is-not-scrollable wds-dropdown__content">
					<ul class="wds-list wds-is-linked">
													
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Superstore_Wiki"
			   data-tracking="explore-main-page"
							>
				<svg class="wds-icon-tiny wds-icon navigation-item-icon"><use xlink:href="#wds-icons-home-tiny"></use></svg>				<span>Main Page</span>
			</a>
		</li>
														
			<li>
			<a href="/f"
			   data-tracking="explore-discuss"
							>
				<svg class="wds-icon-tiny wds-icon navigation-item-icon"><use xlink:href="#wds-icons-discussions-tiny"></use></svg>				<span>Discuss</span>
			</a>
		</li>
														
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Special:AllPages"
			   data-tracking="explore-all-pages"
							>
								<span>All Pages</span>
			</a>
		</li>
														
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Special:Community"
			   data-tracking="explore-community"
							>
								<span>Community</span>
			</a>
		</li>
														
			<li>
			<a href="/Blog:Recent_posts"
			   data-tracking="explore-blogs"
							>
								<span>Recent Blog Posts</span>
			</a>
		</li>
												</ul>
			</div>
		</li>
						
			<li class="wds-tabs__tab ">
			<div class="wds-tabs__tab-label first-level-item">
				<a href="https://superstore-nbc.fandom.com/wiki/Superstore"
				   data-tracking="custom-level-1"
					 				>
										<span>About Superstore</span>
				</a>
			</div>
		</li>
						
			<li class="wds-dropdown ">
			<div class="wds-tabs__tab-label wds-dropdown__toggle first-level-item">
				<a href="https://superstore-nbc.fandom.com/wiki/Category:Characters"
				   data-tracking="custom-level-1"
									>
										<span>Characters</span>
				</a>
				<svg class="wds-icon wds-icon-tiny wds-dropdown__toggle-chevron"><use xlink:href="#wds-icons-dropdown-tiny"></use></svg>			</div>
			<div class="wds-is-not-scrollable wds-dropdown__content">
					<ul class="wds-list wds-is-linked">
													
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Main_Characters"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Main Characters</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Amy_Dubanowski"
			   data-tracking="custom-level-3"
							>
								<span>Amy Sosa</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Jonah_Simms"
			   data-tracking="custom-level-3"
							>
								<span>Jonah Simms</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Glenn_Sturgis"
			   data-tracking="custom-level-3"
							>
								<span>Glenn Sturgis</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Dina_Fox"
			   data-tracking="custom-level-3"
							>
								<span>Dina Fox</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Garrett_McNeill"
			   data-tracking="custom-level-3"
							>
								<span>Garrett McNeill</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cheyenne_Lee"
			   data-tracking="custom-level-3"
							>
								<span>Cheyenne Lee</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Mateo_Liwanag"
			   data-tracking="custom-level-3"
							>
								<span>Mateo Liwanag</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Sandra"
			   data-tracking="custom-level-3"
							>
								<span>Sandra</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Cloud_9_Employees"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Other Employees</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Brett"
			   data-tracking="custom-level-3"
							>
								<span>Brett</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Carol"
			   data-tracking="custom-level-3"
							>
								<span>Carol</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Elias"
			   data-tracking="custom-level-3"
							>
								<span>Elias</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Jeff_Sutin"
			   data-tracking="custom-level-3"
							>
								<span>Jeff Sutin</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Justine"
			   data-tracking="custom-level-3"
							>
								<span>Justine</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Kelly"
			   data-tracking="custom-level-3"
							>
								<span>Kelly</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Marcus"
			   data-tracking="custom-level-3"
							>
								<span>Marcus</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Myrtle"
			   data-tracking="custom-level-3"
							>
								<span>Myrtle</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Tate"
			   data-tracking="custom-level-3"
							>
								<span>Tate</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Cloud_9_Employees"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Minor Employees</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Chris"
			   data-tracking="custom-level-3"
							>
								<span>Chris</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Heather"
			   data-tracking="custom-level-3"
							>
								<span>Heather</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Henry"
			   data-tracking="custom-level-3"
							>
								<span>Henry</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Sarah"
			   data-tracking="custom-level-3"
							>
								<span>Sarah</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Travis"
			   data-tracking="custom-level-3"
							>
								<span>Travis/Tim</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_One_minor_employees"
			   data-tracking="custom-level-3"
							>
								<span>Season One minor employees</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Two_minor_employees"
			   data-tracking="custom-level-3"
							>
								<span>Season Two minor employees</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Three_minor_employees"
			   data-tracking="custom-level-3"
							>
								<span>Season Three minor employees</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Four_minor_employees"
			   data-tracking="custom-level-3"
							>
								<span>Season Four minor employees</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Relatives"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Relatives</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Adam_Dubanowski"
			   data-tracking="custom-level-3"
							>
								<span>Adam Dubanowski</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Bo_Derek_Thompson"
			   data-tracking="custom-level-3"
							>
								<span>Bo Derek Thompson</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Brandi"
			   data-tracking="custom-level-3"
							>
								<span>Brandi</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Emma_Dubanowski"
			   data-tracking="custom-level-3"
							>
								<span>Emma Dubanowski</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Jerusha_Sturgis"
			   data-tracking="custom-level-3"
							>
								<span>Jerusha Sturgis</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Kristen"
			   data-tracking="custom-level-3"
							>
								<span>Kristen</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Leo"
			   data-tracking="custom-level-3"
							>
								<span>Leo</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Ron_Sosa"
			   data-tracking="custom-level-3"
							>
								<span>Ron Sosa</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Timur"
			   data-tracking="custom-level-3"
							>
								<span>Timur</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Zoe"
			   data-tracking="custom-level-3"
							>
								<span>Zoe</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Visitors"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Visitors</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Howie"
			   data-tracking="custom-level-3"
							>
								<span>Howie</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Jerry"
			   data-tracking="custom-level-3"
							>
								<span>Jerry</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Larry"
			   data-tracking="custom-level-3"
							>
								<span>Larry/Bruce</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Missy_Jones"
			   data-tracking="custom-level-3"
							>
								<span>Missy Jones</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Naomi"
			   data-tracking="custom-level-3"
							>
								<span>Naomi</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Nikki"
			   data-tracking="custom-level-3"
							>
								<span>Nikki</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Pastor_Craig"
			   data-tracking="custom-level-3"
							>
								<span>Pastor Craig</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Scott"
			   data-tracking="custom-level-3"
							>
								<span>Scott</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Shannon"
			   data-tracking="custom-level-3"
							>
								<span>Shannon</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Tom"
			   data-tracking="custom-level-3"
							>
								<span>Tom</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Cast"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Main Cast</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/America_Ferrera"
			   data-tracking="custom-level-3"
							>
								<span>America Ferrera</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Ben_Feldman"
			   data-tracking="custom-level-3"
							>
								<span>Ben Feldman</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Mark_McKinney"
			   data-tracking="custom-level-3"
							>
								<span>Mark McKinney</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Lauren_Ash"
			   data-tracking="custom-level-3"
							>
								<span>Lauren Ash</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Colton_Dunn"
			   data-tracking="custom-level-3"
							>
								<span>Colton Dunn</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Nichole_Bloom"
			   data-tracking="custom-level-3"
							>
								<span>Nichole Bloom</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Nico_Santos"
			   data-tracking="custom-level-3"
							>
								<span>Nico Santos</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
												</ul>
			</div>
		</li>
						
			<li class="wds-dropdown ">
			<div class="wds-tabs__tab-label wds-dropdown__toggle first-level-item">
				<a href="https://superstore-nbc.fandom.com/wiki/Category:Episodes"
				   data-tracking="custom-level-1"
									>
										<span>Episodes</span>
				</a>
				<svg class="wds-icon wds-icon-tiny wds-dropdown__toggle-chevron"><use xlink:href="#wds-icons-dropdown-tiny"></use></svg>			</div>
			<div class="wds-is-not-scrollable wds-dropdown__content">
					<ul class="wds-list wds-is-linked">
													
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_One"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 1</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Pilot"
			   data-tracking="custom-level-3"
							>
								<span>Pilot</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Magazine_Profile"
			   data-tracking="custom-level-3"
							>
								<span>Magazine Profile</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Shots_and_Salsa"
			   data-tracking="custom-level-3"
							>
								<span>Shots and Salsa</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Mannequin"
			   data-tracking="custom-level-3"
							>
								<span>Mannequin</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Secret_Shopper"
			   data-tracking="custom-level-3"
							>
								<span>Secret Shopper</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Color_Wars"
			   data-tracking="custom-level-3"
							>
								<span>Color Wars</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Wedding_Day_Sale"
			   data-tracking="custom-level-3"
							>
								<span>Wedding Day Sale</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/All-Nighter"
			   data-tracking="custom-level-3"
							>
								<span>All-Nighter</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Demotion"
			   data-tracking="custom-level-3"
							>
								<span>Demotion</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Labor"
			   data-tracking="custom-level-3"
							>
								<span>Labor</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Two"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 2</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Olympics"
			   data-tracking="custom-level-3"
							>
								<span>Olympics</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Strike"
			   data-tracking="custom-level-3"
							>
								<span>Strike</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Back_to_Work"
			   data-tracking="custom-level-3"
							>
								<span>Back to Work</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Guns,_Pills,_and_Birds"
			   data-tracking="custom-level-3"
							>
								<span>Guns, Pills, and Birds</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Spokesman_Scandal"
			   data-tracking="custom-level-3"
							>
								<span>Spokesman Scandal</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Lost_and_Found"
			   data-tracking="custom-level-3"
							>
								<span>Lost and Found</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Mateo%27s_Last_Day"
			   data-tracking="custom-level-3"
							>
								<span>Mateo's Last Day</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Spring_Cleaning"
			   data-tracking="custom-level-3"
							>
								<span>Spring Cleaning</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cheyenne%27s_Wedding"
			   data-tracking="custom-level-3"
							>
								<span>Cheyenne's Wedding</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Tornado"
			   data-tracking="custom-level-3"
							>
								<span>Tornado</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Three"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 3</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Grand_Re-Opening"
			   data-tracking="custom-level-3"
							>
								<span>Grand Re-Opening</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Brett_Is_Dead"
			   data-tracking="custom-level-3"
							>
								<span>Brett Is Dead</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Workplace_Bullying"
			   data-tracking="custom-level-3"
							>
								<span>Workplace Bullying</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Sal%27s_Dead"
			   data-tracking="custom-level-3"
							>
								<span>Sal's Dead</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/District_Manager"
			   data-tracking="custom-level-3"
							>
								<span>District Manager</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Local_Vendors_Day"
			   data-tracking="custom-level-3"
							>
								<span>Local Vendors Day</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Lottery"
			   data-tracking="custom-level-3"
							>
								<span>Lottery</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Gender_Reveal"
			   data-tracking="custom-level-3"
							>
								<span>Gender Reveal</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Aftermath"
			   data-tracking="custom-level-3"
							>
								<span>Aftermath</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Town_Hall"
			   data-tracking="custom-level-3"
							>
								<span>Town Hall</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Four"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 4</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Back_To_School"
			   data-tracking="custom-level-3"
							>
								<span>Back To School</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Baby_Shower"
			   data-tracking="custom-level-3"
							>
								<span>Baby Shower</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Toxic_Work_Environment"
			   data-tracking="custom-level-3"
							>
								<span>Toxic Work Environment</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Costume_Competition"
			   data-tracking="custom-level-3"
							>
								<span>Costume Competition</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Delivery_Day"
			   data-tracking="custom-level-3"
							>
								<span>Delivery Day</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cloud_Green"
			   data-tracking="custom-level-3"
							>
								<span>Cloud Green</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Scanners"
			   data-tracking="custom-level-3"
							>
								<span>Scanners</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/CLOUD9FAIL"
			   data-tracking="custom-level-3"
							>
								<span>CLOUD9FAIL</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Sandra%27s_Fight"
			   data-tracking="custom-level-3"
							>
								<span>Sandra's Fight</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Employee_Appreciation_Day"
			   data-tracking="custom-level-3"
							>
								<span>Employee Appreciation Day</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Five"
			   data-tracking="custom-level-2"
							>
								<span>Season 5</span>
			</a>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Six"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 6</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Essential"
			   data-tracking="custom-level-3"
							>
								<span>Essential</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/California_Part_2"
			   data-tracking="custom-level-3"
							>
								<span>California Part 2</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Floor_Supervisor"
			   data-tracking="custom-level-3"
							>
								<span>Floor Supervisor</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Prize_Wheel"
			   data-tracking="custom-level-3"
							>
								<span>Prize Wheel</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
												</ul>
			</div>
		</li>
						
			<li class="wds-dropdown ">
			<div class="wds-tabs__tab-label wds-dropdown__toggle first-level-item">
				<a href="https://superstore-nbc.fandom.com/wiki/Category:Superstore"
				   data-tracking="custom-level-1"
									>
										<span>Misc</span>
				</a>
				<svg class="wds-icon wds-icon-tiny wds-dropdown__toggle-chevron"><use xlink:href="#wds-icons-dropdown-tiny"></use></svg>			</div>
			<div class="wds-is-not-scrollable wds-dropdown__content">
					<ul class="wds-list wds-is-linked">
													
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Locations"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Locations</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Amy%27s_house"
			   data-tracking="custom-level-3"
							>
								<span>Amy's house</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Break_Room"
			   data-tracking="custom-level-3"
							>
								<span>Break Room</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cloud_9"
			   data-tracking="custom-level-3"
							>
								<span>Cloud 9</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cloud_9_Store_1217"
			   data-tracking="custom-level-3"
							>
								<span>Cloud 9 Store 1217</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cloud_9_Chesterfield_Store"
			   data-tracking="custom-level-3"
							>
								<span>Cloud 9 Chesterfield Store</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Coffee_%26_Bakery"
			   data-tracking="custom-level-3"
							>
								<span>Coffee & Bakery</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Glenn%27s_Office"
			   data-tracking="custom-level-3"
							>
								<span>Glenn's Office</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Pharmacy"
			   data-tracking="custom-level-3"
							>
								<span>Pharmacy</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Photo_Lab"
			   data-tracking="custom-level-3"
							>
								<span>Photo Lab</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Surveillance_Office"
			   data-tracking="custom-level-3"
							>
								<span>Surveillance Office</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
												</ul>
			</div>
		</li>
				</ul>
</nav>
	<div class="wiki-tools wds-button-group">
				<a
			href="/wiki/Special:Search"
			class="wds-button wds-is-secondary wiki-tools__search"
			title="Search"
			data-tracking="search"
					>
			<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-magnifying-glass-small"></use></svg>		</a>
			<a
			href="/f"
			class="wds-button wds-is-secondary "
			title="Discuss"
			data-tracking="discussions"
					>
			<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-discussions-small"></use></svg>		</a>
			<a
			href="#"
			class="wds-button wds-is-secondary wiki-tools__theme-switch"
			title="Dark Theme"
			data-tracking="theme-switch-dark"
					>
			<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-moon-small"></use></svg>		</a>
		</div>
</div>

<div class="global-navigation">
	<div class="global-navigation__top">
		<nav class="global-navigation__nav" aria-label="Fandom navigation">
			<a
				href="https://www.fandom.com/"
				class="global-navigation__logo"
				data-tracking-label="logo"
				aria-label="Fandom homepage"
			>
				<svg class="wds-icon"><use xlink:href="#wds-brand-fandom-logomark"></use></svg>				<span>FANDOM</span>
			</a>

							<a href="/wiki/Special:Search" class="global-navigation__search global-navigation__icon" accesskey="f"
				   title="Search" data-tracking-label="search"
				   data-wds-tooltip="Search"
				   data-wds-tooltip-position="right"
				>
				<svg class="wds-icon"><use xlink:href="#wds-icons-magnifying-glass"></use></svg>				</a>
			
			
<div class="global-navigation__links">
			<a href="https://www.fandom.com/topics/games" class="global-navigation__link"
		   data-tracking-label="link.games"
		>
			<span class="global-navigation__icon has-background">
				<svg class="wds-icon wds-is-stroke-icon"><use xlink:href="#wds-verticals-games"></use></svg>			</span>
			<span class="global-navigation__label">
				Games			</span>
		</a>
			<a href="https://www.fandom.com/topics/anime" class="global-navigation__link"
		   data-tracking-label="link.anime"
		>
			<span class="global-navigation__icon has-background">
				<svg class="wds-icon wds-is-stroke-icon"><use xlink:href="#wds-verticals-anime"></use></svg>			</span>
			<span class="global-navigation__label">
				Anime			</span>
		</a>
			<a href="https://www.fandom.com/topics/movies" class="global-navigation__link"
		   data-tracking-label="link.movies"
		>
			<span class="global-navigation__icon has-background">
				<svg class="wds-icon wds-is-stroke-icon"><use xlink:href="#wds-verticals-movies"></use></svg>			</span>
			<span class="global-navigation__label">
				Movies			</span>
		</a>
			<a href="https://www.fandom.com/topics/tv" class="global-navigation__link"
		   data-tracking-label="link.tv"
		>
			<span class="global-navigation__icon has-background">
				<svg class="wds-icon wds-is-stroke-icon"><use xlink:href="#wds-verticals-tv"></use></svg>			</span>
			<span class="global-navigation__label">
				TV			</span>
		</a>
			<a href="https://www.fandom.com/video" class="global-navigation__link"
		   data-tracking-label="link.video"
		>
			<span class="global-navigation__icon has-background">
				<svg class="wds-icon wds-is-stroke-icon"><use xlink:href="#wds-verticals-video"></use></svg>			</span>
			<span class="global-navigation__label">
				Video			</span>
		</a>
	
			<div class="wds-dropdown wds-open-to-right">
			<div class="wds-dropdown__toggle"
				 data-tracking-label="link.wikis">
				<div class="global-navigation__icon has-background">
					<svg class="wds-icon wds-is-stroke-icon"><use xlink:href="#wds-verticals-wikis"></use></svg>				</div>
				<div class="global-navigation__label">
					Wikis				</div>
			</div>
			<div class="wds-dropdown__content">
				<ul class="wds-list wds-is-linked">
											<li>
							<a href="https://www.fandom.com/explore"
							   data-tracking-label="link.explore">
								Explore Wikis							</a>
						</li>
											<li>
							<a href="//community.fandom.com/wiki/Community_Central"
							   data-tracking-label="link.community-central">
								Community Central							</a>
						</li>
									</ul>
			</div>
		</div>
	
			<a href="//community.fandom.com/wiki/Special:CreateNewWiki" class="global-navigation__link"
		   data-tracking-label="start-a-wiki"
		>
			<span class="global-navigation__icon has-border">
				<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-add-small"></use></svg>			</span>
			<span class="global-navigation__label">
				Start a Wiki			</span>
		</a>
	</div>
		</nav>
	</div>

	<div class="global-navigation__bottom">
							
<div class="wds-dropdown wds-open-to-right is-attached-to-bottom is-anon-dropdown">
	<div class="wds-dropdown__toggle">
		<div class="global-navigation__icon">
			<svg class="wds-icon"><use xlink:href="#wds-icons-avatar"></use></svg>		</div>
	</div>
	<div class="wds-dropdown__content">
		<a class="wds-button wds-is-full-width wds-is-secondary"
		   href="https://www.fandom.com/register?redirect=https%3A%2F%2Fsuperstore-nbc.fandom.com%2Fwiki%2FCategory%3ATranscripts"
		   rel="nofollow"
		   data-tracking-label="account.register"
		   id="global-navigation-register-link">
			Register		</a>
		<div class="global-navigation__register-text">
			Don&#039;t have an account?		</div>
		<hr>
		<a class="wds-button wds-is-full-width"
		   href="https://www.fandom.com/signin?redirect=https%3A%2F%2Fsuperstore-nbc.fandom.com%2Fwiki%2FCategory%3ATranscripts"
		   rel="nofollow"
		   data-tracking-label="account.sign-in"
		   id="global-navigation-sign-in-link">
			Sign In		</a>
	</div>
</div>
			</div>
</div>
<div class="main-container">
	
	<div class="top-ads-container">
		<div class="ad-slot-placeholder top-leaderboard is-loading"></div>
		<div class="ae-translatable-label" data-key="advertisement">Advertisement</div>
	</div>
	<div class="fandom-community-header__background cover header " style="--image-ratio:0.22777777777778"></div>
	<div class="resizable-container">
		<div class="community-header-wrapper" >
	<header class="fandom-community-header">
					<a accesskey="z" href="//superstore-nbc.fandom.com" class="fandom-community-header__image">
				<img
					 src="https://static.wikia.nocookie.net/superstore-nbc/images/e/e6/Site-logo.png/revision/latest?cb=20210714141104"
					 width="250"
					 height="65"
					 alt="Superstore Wiki"
					 data-test="fandom-community-header-community-logo">
			</a>
				<div class="fandom-community-header__top-container">
			<div class="fandom-community-header__community-name-wrapper">
				<a href="//superstore-nbc.fandom.com" class="fandom-community-header__community-name"
				   data-test="fandom-community-header-cummunity-name">
					Let's get our shift together.				</a>
											</div>
			<div class="page-counter">
				<div class="page-counter__value">509</div><div class="page-counter__label">pages</div>			</div>
			<div class="wiki-tools wds-button-group">
				<a
			href="/wiki/Special:Search"
			class="wds-button wds-is-secondary wiki-tools__search"
			title="Search"
			data-tracking="search"
					>
			<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-magnifying-glass-small"></use></svg>		</a>
			<a
			href="/f"
			class="wds-button wds-is-secondary "
			title="Discuss"
			data-tracking="discussions"
					>
			<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-discussions-small"></use></svg>		</a>
			<a
			href="#"
			class="wds-button wds-is-secondary wiki-tools__theme-switch"
			title="Dark Theme"
			data-tracking="theme-switch-dark"
					>
			<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-moon-small"></use></svg>		</a>
		</div>
		</div>
		
<nav class="fandom-community-header__local-navigation">
	<ul class="wds-tabs">
					
			<li class="wds-dropdown explore-menu">
			<div class="wds-tabs__tab-label wds-dropdown__toggle first-level-item">
				<a href="#"
				   data-tracking="custom-level-1"
									>
					<svg class="wds-icon-tiny wds-icon"><use xlink:href="#wds-icons-book-tiny"></use></svg>					<span>Explore</span>
				</a>
				<svg class="wds-icon wds-icon-tiny wds-dropdown__toggle-chevron"><use xlink:href="#wds-icons-dropdown-tiny"></use></svg>			</div>
			<div class="wds-is-not-scrollable wds-dropdown__content">
					<ul class="wds-list wds-is-linked">
													
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Superstore_Wiki"
			   data-tracking="explore-main-page"
							>
				<svg class="wds-icon-tiny wds-icon navigation-item-icon"><use xlink:href="#wds-icons-home-tiny"></use></svg>				<span>Main Page</span>
			</a>
		</li>
														
			<li>
			<a href="/f"
			   data-tracking="explore-discuss"
							>
				<svg class="wds-icon-tiny wds-icon navigation-item-icon"><use xlink:href="#wds-icons-discussions-tiny"></use></svg>				<span>Discuss</span>
			</a>
		</li>
														
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Special:AllPages"
			   data-tracking="explore-all-pages"
							>
								<span>All Pages</span>
			</a>
		</li>
														
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Special:Community"
			   data-tracking="explore-community"
							>
								<span>Community</span>
			</a>
		</li>
														
			<li>
			<a href="/Blog:Recent_posts"
			   data-tracking="explore-blogs"
							>
								<span>Recent Blog Posts</span>
			</a>
		</li>
												</ul>
			</div>
		</li>
						
			<li class="wds-tabs__tab ">
			<div class="wds-tabs__tab-label first-level-item">
				<a href="https://superstore-nbc.fandom.com/wiki/Superstore"
				   data-tracking="custom-level-1"
					 				>
										<span>About Superstore</span>
				</a>
			</div>
		</li>
						
			<li class="wds-dropdown ">
			<div class="wds-tabs__tab-label wds-dropdown__toggle first-level-item">
				<a href="https://superstore-nbc.fandom.com/wiki/Category:Characters"
				   data-tracking="custom-level-1"
									>
										<span>Characters</span>
				</a>
				<svg class="wds-icon wds-icon-tiny wds-dropdown__toggle-chevron"><use xlink:href="#wds-icons-dropdown-tiny"></use></svg>			</div>
			<div class="wds-is-not-scrollable wds-dropdown__content">
					<ul class="wds-list wds-is-linked">
													
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Main_Characters"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Main Characters</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Amy_Dubanowski"
			   data-tracking="custom-level-3"
							>
								<span>Amy Sosa</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Jonah_Simms"
			   data-tracking="custom-level-3"
							>
								<span>Jonah Simms</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Glenn_Sturgis"
			   data-tracking="custom-level-3"
							>
								<span>Glenn Sturgis</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Dina_Fox"
			   data-tracking="custom-level-3"
							>
								<span>Dina Fox</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Garrett_McNeill"
			   data-tracking="custom-level-3"
							>
								<span>Garrett McNeill</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cheyenne_Lee"
			   data-tracking="custom-level-3"
							>
								<span>Cheyenne Lee</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Mateo_Liwanag"
			   data-tracking="custom-level-3"
							>
								<span>Mateo Liwanag</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Sandra"
			   data-tracking="custom-level-3"
							>
								<span>Sandra</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Cloud_9_Employees"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Other Employees</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Brett"
			   data-tracking="custom-level-3"
							>
								<span>Brett</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Carol"
			   data-tracking="custom-level-3"
							>
								<span>Carol</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Elias"
			   data-tracking="custom-level-3"
							>
								<span>Elias</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Jeff_Sutin"
			   data-tracking="custom-level-3"
							>
								<span>Jeff Sutin</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Justine"
			   data-tracking="custom-level-3"
							>
								<span>Justine</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Kelly"
			   data-tracking="custom-level-3"
							>
								<span>Kelly</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Marcus"
			   data-tracking="custom-level-3"
							>
								<span>Marcus</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Myrtle"
			   data-tracking="custom-level-3"
							>
								<span>Myrtle</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Tate"
			   data-tracking="custom-level-3"
							>
								<span>Tate</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Cloud_9_Employees"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Minor Employees</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Chris"
			   data-tracking="custom-level-3"
							>
								<span>Chris</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Heather"
			   data-tracking="custom-level-3"
							>
								<span>Heather</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Henry"
			   data-tracking="custom-level-3"
							>
								<span>Henry</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Sarah"
			   data-tracking="custom-level-3"
							>
								<span>Sarah</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Travis"
			   data-tracking="custom-level-3"
							>
								<span>Travis/Tim</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_One_minor_employees"
			   data-tracking="custom-level-3"
							>
								<span>Season One minor employees</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Two_minor_employees"
			   data-tracking="custom-level-3"
							>
								<span>Season Two minor employees</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Three_minor_employees"
			   data-tracking="custom-level-3"
							>
								<span>Season Three minor employees</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Four_minor_employees"
			   data-tracking="custom-level-3"
							>
								<span>Season Four minor employees</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Relatives"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Relatives</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Adam_Dubanowski"
			   data-tracking="custom-level-3"
							>
								<span>Adam Dubanowski</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Bo_Derek_Thompson"
			   data-tracking="custom-level-3"
							>
								<span>Bo Derek Thompson</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Brandi"
			   data-tracking="custom-level-3"
							>
								<span>Brandi</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Emma_Dubanowski"
			   data-tracking="custom-level-3"
							>
								<span>Emma Dubanowski</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Jerusha_Sturgis"
			   data-tracking="custom-level-3"
							>
								<span>Jerusha Sturgis</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Kristen"
			   data-tracking="custom-level-3"
							>
								<span>Kristen</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Leo"
			   data-tracking="custom-level-3"
							>
								<span>Leo</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Ron_Sosa"
			   data-tracking="custom-level-3"
							>
								<span>Ron Sosa</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Timur"
			   data-tracking="custom-level-3"
							>
								<span>Timur</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Zoe"
			   data-tracking="custom-level-3"
							>
								<span>Zoe</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Visitors"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Visitors</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Howie"
			   data-tracking="custom-level-3"
							>
								<span>Howie</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Jerry"
			   data-tracking="custom-level-3"
							>
								<span>Jerry</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Larry"
			   data-tracking="custom-level-3"
							>
								<span>Larry/Bruce</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Missy_Jones"
			   data-tracking="custom-level-3"
							>
								<span>Missy Jones</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Naomi"
			   data-tracking="custom-level-3"
							>
								<span>Naomi</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Nikki"
			   data-tracking="custom-level-3"
							>
								<span>Nikki</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Pastor_Craig"
			   data-tracking="custom-level-3"
							>
								<span>Pastor Craig</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Scott"
			   data-tracking="custom-level-3"
							>
								<span>Scott</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Shannon"
			   data-tracking="custom-level-3"
							>
								<span>Shannon</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Tom"
			   data-tracking="custom-level-3"
							>
								<span>Tom</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Cast"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Main Cast</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/America_Ferrera"
			   data-tracking="custom-level-3"
							>
								<span>America Ferrera</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Ben_Feldman"
			   data-tracking="custom-level-3"
							>
								<span>Ben Feldman</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Mark_McKinney"
			   data-tracking="custom-level-3"
							>
								<span>Mark McKinney</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Lauren_Ash"
			   data-tracking="custom-level-3"
							>
								<span>Lauren Ash</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Colton_Dunn"
			   data-tracking="custom-level-3"
							>
								<span>Colton Dunn</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Nichole_Bloom"
			   data-tracking="custom-level-3"
							>
								<span>Nichole Bloom</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Nico_Santos"
			   data-tracking="custom-level-3"
							>
								<span>Nico Santos</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
												</ul>
			</div>
		</li>
						
			<li class="wds-dropdown ">
			<div class="wds-tabs__tab-label wds-dropdown__toggle first-level-item">
				<a href="https://superstore-nbc.fandom.com/wiki/Category:Episodes"
				   data-tracking="custom-level-1"
									>
										<span>Episodes</span>
				</a>
				<svg class="wds-icon wds-icon-tiny wds-dropdown__toggle-chevron"><use xlink:href="#wds-icons-dropdown-tiny"></use></svg>			</div>
			<div class="wds-is-not-scrollable wds-dropdown__content">
					<ul class="wds-list wds-is-linked">
													
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_One"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 1</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Pilot"
			   data-tracking="custom-level-3"
							>
								<span>Pilot</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Magazine_Profile"
			   data-tracking="custom-level-3"
							>
								<span>Magazine Profile</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Shots_and_Salsa"
			   data-tracking="custom-level-3"
							>
								<span>Shots and Salsa</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Mannequin"
			   data-tracking="custom-level-3"
							>
								<span>Mannequin</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Secret_Shopper"
			   data-tracking="custom-level-3"
							>
								<span>Secret Shopper</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Color_Wars"
			   data-tracking="custom-level-3"
							>
								<span>Color Wars</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Wedding_Day_Sale"
			   data-tracking="custom-level-3"
							>
								<span>Wedding Day Sale</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/All-Nighter"
			   data-tracking="custom-level-3"
							>
								<span>All-Nighter</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Demotion"
			   data-tracking="custom-level-3"
							>
								<span>Demotion</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Labor"
			   data-tracking="custom-level-3"
							>
								<span>Labor</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Two"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 2</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Olympics"
			   data-tracking="custom-level-3"
							>
								<span>Olympics</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Strike"
			   data-tracking="custom-level-3"
							>
								<span>Strike</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Back_to_Work"
			   data-tracking="custom-level-3"
							>
								<span>Back to Work</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Guns,_Pills,_and_Birds"
			   data-tracking="custom-level-3"
							>
								<span>Guns, Pills, and Birds</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Spokesman_Scandal"
			   data-tracking="custom-level-3"
							>
								<span>Spokesman Scandal</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Lost_and_Found"
			   data-tracking="custom-level-3"
							>
								<span>Lost and Found</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Mateo%27s_Last_Day"
			   data-tracking="custom-level-3"
							>
								<span>Mateo's Last Day</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Spring_Cleaning"
			   data-tracking="custom-level-3"
							>
								<span>Spring Cleaning</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cheyenne%27s_Wedding"
			   data-tracking="custom-level-3"
							>
								<span>Cheyenne's Wedding</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Tornado"
			   data-tracking="custom-level-3"
							>
								<span>Tornado</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Three"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 3</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Grand_Re-Opening"
			   data-tracking="custom-level-3"
							>
								<span>Grand Re-Opening</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Brett_Is_Dead"
			   data-tracking="custom-level-3"
							>
								<span>Brett Is Dead</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Workplace_Bullying"
			   data-tracking="custom-level-3"
							>
								<span>Workplace Bullying</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Sal%27s_Dead"
			   data-tracking="custom-level-3"
							>
								<span>Sal's Dead</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/District_Manager"
			   data-tracking="custom-level-3"
							>
								<span>District Manager</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Local_Vendors_Day"
			   data-tracking="custom-level-3"
							>
								<span>Local Vendors Day</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Lottery"
			   data-tracking="custom-level-3"
							>
								<span>Lottery</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Gender_Reveal"
			   data-tracking="custom-level-3"
							>
								<span>Gender Reveal</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Aftermath"
			   data-tracking="custom-level-3"
							>
								<span>Aftermath</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Town_Hall"
			   data-tracking="custom-level-3"
							>
								<span>Town Hall</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Four"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 4</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Back_To_School"
			   data-tracking="custom-level-3"
							>
								<span>Back To School</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Baby_Shower"
			   data-tracking="custom-level-3"
							>
								<span>Baby Shower</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Toxic_Work_Environment"
			   data-tracking="custom-level-3"
							>
								<span>Toxic Work Environment</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Costume_Competition"
			   data-tracking="custom-level-3"
							>
								<span>Costume Competition</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Delivery_Day"
			   data-tracking="custom-level-3"
							>
								<span>Delivery Day</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cloud_Green"
			   data-tracking="custom-level-3"
							>
								<span>Cloud Green</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Scanners"
			   data-tracking="custom-level-3"
							>
								<span>Scanners</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/CLOUD9FAIL"
			   data-tracking="custom-level-3"
							>
								<span>CLOUD9FAIL</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Sandra%27s_Fight"
			   data-tracking="custom-level-3"
							>
								<span>Sandra's Fight</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Employee_Appreciation_Day"
			   data-tracking="custom-level-3"
							>
								<span>Employee Appreciation Day</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
														
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Five"
			   data-tracking="custom-level-2"
							>
								<span>Season 5</span>
			</a>
		</li>
														
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Season_Six"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Season 6</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Essential"
			   data-tracking="custom-level-3"
							>
								<span>Essential</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/California_Part_2"
			   data-tracking="custom-level-3"
							>
								<span>California Part 2</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Floor_Supervisor"
			   data-tracking="custom-level-3"
							>
								<span>Floor Supervisor</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Prize_Wheel"
			   data-tracking="custom-level-3"
							>
								<span>Prize Wheel</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
												</ul>
			</div>
		</li>
						
			<li class="wds-dropdown ">
			<div class="wds-tabs__tab-label wds-dropdown__toggle first-level-item">
				<a href="https://superstore-nbc.fandom.com/wiki/Category:Superstore"
				   data-tracking="custom-level-1"
									>
										<span>Misc</span>
				</a>
				<svg class="wds-icon wds-icon-tiny wds-dropdown__toggle-chevron"><use xlink:href="#wds-icons-dropdown-tiny"></use></svg>			</div>
			<div class="wds-is-not-scrollable wds-dropdown__content">
					<ul class="wds-list wds-is-linked">
													
			<li class="wds-dropdown-level-nested">
			<a href="https://superstore-nbc.fandom.com/wiki/Category:Locations"
			   class="wds-dropdown-level-nested__toggle"
			   data-tracking="custom-level-2"
							>
								<span>Locations</span>
				<svg class="wds-icon wds-icon-tiny wds-dropdown-chevron"><use xlink:href="#wds-icons-menu-control-tiny"></use></svg>			</a>
			<div class="wds-is-not-scrollable wds-dropdown-level-nested__content">
				<ul class="wds-list wds-is-linked">
											
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Amy%27s_house"
			   data-tracking="custom-level-3"
							>
								<span>Amy's house</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Break_Room"
			   data-tracking="custom-level-3"
							>
								<span>Break Room</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cloud_9"
			   data-tracking="custom-level-3"
							>
								<span>Cloud 9</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cloud_9_Store_1217"
			   data-tracking="custom-level-3"
							>
								<span>Cloud 9 Store 1217</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Cloud_9_Chesterfield_Store"
			   data-tracking="custom-level-3"
							>
								<span>Cloud 9 Chesterfield Store</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Coffee_%26_Bakery"
			   data-tracking="custom-level-3"
							>
								<span>Coffee & Bakery</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Glenn%27s_Office"
			   data-tracking="custom-level-3"
							>
								<span>Glenn's Office</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Pharmacy"
			   data-tracking="custom-level-3"
							>
								<span>Pharmacy</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Photo_Lab"
			   data-tracking="custom-level-3"
							>
								<span>Photo Lab</span>
			</a>
		</li>
												
			<li>
			<a href="https://superstore-nbc.fandom.com/wiki/Surveillance_Office"
			   data-tracking="custom-level-3"
							>
								<span>Surveillance Office</span>
			</a>
		</li>
										</ul>
			</div>
		</li>
												</ul>
			</div>
		</li>
				</ul>
</nav>
	</header>
</div>
		<div class="page has-right-rail">
			<main class="page__main" lang="en">
				<div class="page-side-tools__wrapper">
					<div class="page-side-tools">
						<button class="page-side-tool content-size-toggle">
															<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-zoom-in-small"></use></svg>													</button>
													<a class="page-side-tool page-side-edit" href="/wiki/Category:Transcripts?action=edit"
								id="ca-viewsource-side-tool"
								data-tracking-label="ca-viewsource"
								data-wds-tooltip="View source"
								data-wds-tooltip-position="right"
							>
								<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-lock-small"></use></svg>							</a>
											</div>
				</div>
				
	<div class="page-header">
		<div class="page-header__top">
			<div class="page-header__meta">
								
			</div>
								</div>
		<div class="page-header__bottom">
			<div class="page-header__title-wrapper">
				<h1 class="page-header__title" id="firstHeading">
					Transcripts				</h1>
															<div class="page-header__page-subtitle">Category page</div>
												</div>
			<div class="page-header__actions" id="p-views">
				
				
									<a class="wds-button wds-is-text page-header__action-button has-label" href="/wiki/Category:Transcripts?action=edit"
					   id="ca-viewsource"
					   data-tracking-label="ca-viewsource"
							accesskey="e"					>
						<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-lock-small"></use></svg>						View source					</a>
				
				
									<div class="wds-dropdown">
						<div class="wds-dropdown__toggle wds-button wds-is-text page-header__action-button">
							<svg class="wds-icon wds-icon-small"><use xlink:href="#wds-icons-more-small"></use></svg>						</div>
						<div id="p-cactions" class="wds-dropdown__content wds-is-right-aligned wds-is-not-scrollable">
							<ul class="wds-list wds-is-linked">
																	<li>
										<a id="ca-history"
										   href="/wiki/Category:Transcripts?action=history"
																					   data-tracking-label="ca-history-dropdown"
											accesskey="h">
											History										</a>
									</li>
																	<li>
										<a id="ca-talk"
										   href="/wiki/Category_talk:Transcripts?action=edit&amp;redlink=1"
											class="new"										   data-tracking-label="ca-talk-dropdown"
											accesskey="t">
											Talk (0)										</a>
									</li>
															</ul>
						</div>
					</div>
					<script type="application/javascript">
						window.RLQ = window.RLQ || [];
						window.RLQ.push(() => {
							mw.config.set('wgPageActions', {"3":{"class":false,"text":"History","href":"\/wiki\/Category:Transcripts?action=history","id":"ca-history","accesskey":"h","data-tracking":"ca-history-dropdown"},"11":{"class":"new","text":"Talk (0)","href":"\/wiki\/Category_talk:Transcripts?action=edit&redlink=1","exists":false,"primary":true,"context":"talk","rel":"discussion","id":"ca-talk","accesskey":"t","data-tracking":"ca-talk-dropdown"}});
						})
					</script>
											</div>
		</div>
	</div>
				<div id="content" class="page-content">
															<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N6XD44P" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
<div class="mw-parser-output"><p>A directory of episode transcripts.
</p>
<!-- 
NewPP limit report
Cached time: 20220404180835
Cache expiry: 1209600
Dynamic content: false
CPU time usage: 0.001 seconds
Real time usage: 0.001 seconds
Preprocessor visited node count: 1/1000000
Preprocessor generated node count: 0/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 1/40
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 -total
-->

<!-- Saved in parser cache with key prod:superstorenbc:pcache:idhash:3101-0!canonical!FandomDesktop!LegacyGalleries and timestamp 20220404180835 and revision id 23982
 -->
</div><div class="category-page__trending-pages-header">Trending pages</div>
<p class="category-page__total-number">
		All items (84)</p>
<ul class="category-page__alphabet-shortcuts">
			<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM=">#</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1B">A</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1C">B</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1D">C</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1E">D</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1F">E</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1G">F</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1H">G</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1I">H</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1J">I</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1K">J</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1L">K</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1M">L</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1N">M</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1O">N</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1P">O</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1Q">P</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1R">Q</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1S">R</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1T">S</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1U">T</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1V">U</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1W">V</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1X">W</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1Y">X</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1Z">Y</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT1a">Z</a></li>
					<li class="category-page__alphabet-shortcut">
			<a rel="nofollow" data-uncrawlable-url="aHR0cHM6Ly9zdXBlcnN0b3JlLW5iYy5mYW5kb20uY29tL3dpa2kvQ2F0ZWdvcnk6VHJhbnNjcmlwdHM/ZnJvbT0lQzIlQTE=">Other</a></li>
			</ul>
<div class="category-page__members">
				<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					A				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Aftermath/Transcript" class="category-page__member-link" title="Aftermath/Transcript">Aftermath/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/All-Nighter/Transcript" class="category-page__member-link" title="All-Nighter/Transcript">All-Nighter/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Amnesty/Transcript" class="category-page__member-link" title="Amnesty/Transcript">Amnesty/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Angels_and_Mermaids/Transcript" class="category-page__member-link" title="Angels and Mermaids/Transcript">Angels and Mermaids/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					B				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Baby_Shower/Transcript" class="category-page__member-link" title="Baby Shower/Transcript">Baby Shower/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Back_To_School/Transcript" class="category-page__member-link" title="Back To School/Transcript">Back To School/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Back_to_Work/Transcript" class="category-page__member-link" title="Back to Work/Transcript">Back to Work/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Black_Friday/Transcript" class="category-page__member-link" title="Black Friday/Transcript">Black Friday/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Blizzard/Transcript" class="category-page__member-link" title="Blizzard/Transcript">Blizzard/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Brett_Is_Dead/Transcript" class="category-page__member-link" title="Brett Is Dead/Transcript">Brett Is Dead/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					C				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Cheyenne%27s_Wedding/Transcript" class="category-page__member-link" title="Cheyenne&#039;s Wedding/Transcript">Cheyenne&#039;s Wedding/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Christmas_Eve/Transcript" class="category-page__member-link" title="Christmas Eve/Transcript">Christmas Eve/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Cloud_9_Academy/Transcript" class="category-page__member-link" title="Cloud 9 Academy/Transcript">Cloud 9 Academy/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																						<a href="/wiki/Cloud_9.0/Transcript" title="Cloud 9.0/Transcript">
									<img src="https://static.wikia.nocookie.net/superstore-nbc/images/d/d9/NUP_187999_1391.jpeg/revision/latest/smart/width/40/height/30?cb=20190915154807"
										 data-src="https://static.wikia.nocookie.net/superstore-nbc/images/d/d9/NUP_187999_1391.jpeg/revision/latest/smart/width/40/height/30?cb=20190915154807"
										 alt="Cloud 9.0/Transcript"
										 class="category-page__member-thumbnail "
										 onload=""
									>
									<noscript><img src="https://static.wikia.nocookie.net/superstore-nbc/images/d/d9/NUP_187999_1391.jpeg/revision/latest/smart/width/40/height/30?cb=20190915154807"
										 alt="Cloud 9.0/Transcript"
										 class="category-page__member-thumbnail"
									></noscript>
								</a>
													</div>
						<a href="/wiki/Cloud_9.0/Transcript" class="category-page__member-link" title="Cloud 9.0/Transcript">Cloud 9.0/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Cloud_Green/Transcript" class="category-page__member-link" title="Cloud Green/Transcript">Cloud Green/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/CLOUD9FAIL/Transcript" class="category-page__member-link" title="CLOUD9FAIL/Transcript">CLOUD9FAIL/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Color_Wars/Transcript" class="category-page__member-link" title="Color Wars/Transcript">Color Wars/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Costume_Competition/Transcript" class="category-page__member-link" title="Costume Competition/Transcript">Costume Competition/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					D				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Delivery_Day/Transcript" class="category-page__member-link" title="Delivery Day/Transcript">Delivery Day/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Demotion/Transcript" class="category-page__member-link" title="Demotion/Transcript">Demotion/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/District_Manager/Transcript" class="category-page__member-link" title="District Manager/Transcript">District Manager/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Dog_Adoption_Day/Transcript" class="category-page__member-link" title="Dog Adoption Day/Transcript">Dog Adoption Day/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					E				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Easter/Transcript" class="category-page__member-link" title="Easter/Transcript">Easter/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Election_Day/Transcript" class="category-page__member-link" title="Election Day/Transcript">Election Day/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Employee_Appreciation_Day/Transcript" class="category-page__member-link" title="Employee Appreciation Day/Transcript">Employee Appreciation Day/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					F				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																						<a href="/wiki/Forced_Hire/Transcript" title="Forced Hire/Transcript">
									<img src="https://static.wikia.nocookie.net/superstore-nbc/images/f/f5/NUP_188211_0347.jpg/revision/latest/smart/width/40/height/30?cb=20191010215922"
										 data-src="https://static.wikia.nocookie.net/superstore-nbc/images/f/f5/NUP_188211_0347.jpg/revision/latest/smart/width/40/height/30?cb=20191010215922"
										 alt="Forced Hire/Transcript"
										 class="category-page__member-thumbnail "
										 onload=""
									>
									<noscript><img src="https://static.wikia.nocookie.net/superstore-nbc/images/f/f5/NUP_188211_0347.jpg/revision/latest/smart/width/40/height/30?cb=20191010215922"
										 alt="Forced Hire/Transcript"
										 class="category-page__member-thumbnail"
									></noscript>
								</a>
													</div>
						<a href="/wiki/Forced_Hire/Transcript" class="category-page__member-link" title="Forced Hire/Transcript">Forced Hire/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					G				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Gender_Reveal/Transcript" class="category-page__member-link" title="Gender Reveal/Transcript">Gender Reveal/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Glenn%27s_Kids/Transcript" class="category-page__member-link" title="Glenn&#039;s Kids/Transcript">Glenn&#039;s Kids/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Golden_Globes_Party/Transcript" class="category-page__member-link" title="Golden Globes Party/Transcript">Golden Globes Party/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Grand_Re-Opening/Transcript" class="category-page__member-link" title="Grand Re-Opening/Transcript">Grand Re-Opening/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Groundhog_Day/Transcript" class="category-page__member-link" title="Groundhog Day/Transcript">Groundhog Day/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Guns,_Pills,_and_Birds/Transcript" class="category-page__member-link" title="Guns, Pills, and Birds/Transcript">Guns, Pills, and Birds/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					H				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Halloween_Theft/Transcript" class="category-page__member-link" title="Halloween Theft/Transcript">Halloween Theft/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Health_Fund/Transcript" class="category-page__member-link" title="Health Fund/Transcript">Health Fund/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/High_Volume_Store/Transcript" class="category-page__member-link" title="High Volume Store/Transcript">High Volume Store/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					I				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Integrity_Award/Transcript" class="category-page__member-link" title="Integrity Award/Transcript">Integrity Award/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					L				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Labor/Transcript" class="category-page__member-link" title="Labor/Transcript">Labor/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Ladies%27_Lunch/Transcript" class="category-page__member-link" title="Ladies&#039; Lunch/Transcript">Ladies&#039; Lunch/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Local_Vendors_Day/Transcript" class="category-page__member-link" title="Local Vendors Day/Transcript">Local Vendors Day/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Lost_and_Found/Transcript" class="category-page__member-link" title="Lost and Found/Transcript">Lost and Found/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Lottery/Transcript" class="category-page__member-link" title="Lottery/Transcript">Lottery/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Lovebirds/Transcript" class="category-page__member-link" title="Lovebirds/Transcript">Lovebirds/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					M				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Magazine_Profile/Transcript" class="category-page__member-link" title="Magazine Profile/Transcript">Magazine Profile/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																						<a href="/wiki/Mall_Closing/Transcript" title="Mall Closing/Transcript">
									<img src="https://static.wikia.nocookie.net/superstore-nbc/images/e/ea/NUP_188418_0025.jpeg/revision/latest/smart/width/40/height/30?cb=20191016230940"
										 data-src="https://static.wikia.nocookie.net/superstore-nbc/images/e/ea/NUP_188418_0025.jpeg/revision/latest/smart/width/40/height/30?cb=20191016230940"
										 alt="Mall Closing/Transcript"
										 class="category-page__member-thumbnail "
										 onload=""
									>
									<noscript><img src="https://static.wikia.nocookie.net/superstore-nbc/images/e/ea/NUP_188418_0025.jpeg/revision/latest/smart/width/40/height/30?cb=20191016230940"
										 alt="Mall Closing/Transcript"
										 class="category-page__member-thumbnail"
									></noscript>
								</a>
													</div>
						<a href="/wiki/Mall_Closing/Transcript" class="category-page__member-link" title="Mall Closing/Transcript">Mall Closing/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Managers%27_Conference/Transcript" class="category-page__member-link" title="Managers&#039; Conference/Transcript">Managers&#039; Conference/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Mannequin/Transcript" class="category-page__member-link" title="Mannequin/Transcript">Mannequin/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																						<a href="/wiki/Mateo%27s_Last_Day" title="Mateo&#039;s Last Day">
									<img src="https://static.wikia.nocookie.net/superstore-nbc/images/d/dc/S02E17-Mateo_and_Cloud_9_sign.jpg/revision/latest/smart/width/40/height/30?cb=20170902173616"
										 data-src="https://static.wikia.nocookie.net/superstore-nbc/images/d/dc/S02E17-Mateo_and_Cloud_9_sign.jpg/revision/latest/smart/width/40/height/30?cb=20170902173616"
										 alt="Mateo&#039;s Last Day"
										 class="category-page__member-thumbnail "
										 onload=""
									>
									<noscript><img src="https://static.wikia.nocookie.net/superstore-nbc/images/d/dc/S02E17-Mateo_and_Cloud_9_sign.jpg/revision/latest/smart/width/40/height/30?cb=20170902173616"
										 alt="Mateo&#039;s Last Day"
										 class="category-page__member-thumbnail"
									></noscript>
								</a>
													</div>
						<a href="/wiki/Mateo%27s_Last_Day" class="category-page__member-link" title="Mateo&#039;s Last Day">Mateo&#039;s Last Day</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Mateo%27s_Last_Day/Transcript" class="category-page__member-link" title="Mateo&#039;s Last Day/Transcript">Mateo&#039;s Last Day/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Maternity_Leave/Transcript" class="category-page__member-link" title="Maternity Leave/Transcript">Maternity Leave/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Minor_Crimes/Transcript" class="category-page__member-link" title="Minor Crimes/Transcript">Minor Crimes/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					N				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/New_Initiative/Transcript" class="category-page__member-link" title="New Initiative/Transcript">New Initiative/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					O				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Olympics/Transcript" class="category-page__member-link" title="Olympics/Transcript">Olympics/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					P				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Part-Time_Hires/Transcript" class="category-page__member-link" title="Part-Time Hires/Transcript">Part-Time Hires/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Pilot/Transcript" class="category-page__member-link" title="Pilot/Transcript">Pilot/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					Q				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Quincea%C3%B1era/Transcript" class="category-page__member-link" title="Quinceañera/Transcript">Quinceañera/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					R				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Rebranding/Transcript" class="category-page__member-link" title="Rebranding/Transcript">Rebranding/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					S				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Safety_Training/Transcript" class="category-page__member-link" title="Safety Training/Transcript">Safety Training/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Sal%27s_Dead/Transcript" class="category-page__member-link" title="Sal&#039;s Dead/Transcript">Sal&#039;s Dead/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Salary/Transcript" class="category-page__member-link" title="Salary/Transcript">Salary/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Sandra%27s_Fight/Transcript" class="category-page__member-link" title="Sandra&#039;s Fight/Transcript">Sandra&#039;s Fight/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Scanners/Transcript" class="category-page__member-link" title="Scanners/Transcript">Scanners/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Seasonal_Help/Transcript" class="category-page__member-link" title="Seasonal Help/Transcript">Seasonal Help/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Secret_Shopper/Transcript" class="category-page__member-link" title="Secret Shopper/Transcript">Secret Shopper/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																						<a href="/wiki/Self_Care/Transcript" title="Self Care/Transcript">
									<img src="https://static.wikia.nocookie.net/superstore-nbc/images/4/4a/NUP_188244_2100.jpg/revision/latest/smart/width/40/height/30?cb=20191021211315"
										 data-src="https://static.wikia.nocookie.net/superstore-nbc/images/4/4a/NUP_188244_2100.jpg/revision/latest/smart/width/40/height/30?cb=20191021211315"
										 alt="Self Care/Transcript"
										 class="category-page__member-thumbnail "
										 onload=""
									>
									<noscript><img src="https://static.wikia.nocookie.net/superstore-nbc/images/4/4a/NUP_188244_2100.jpg/revision/latest/smart/width/40/height/30?cb=20191021211315"
										 alt="Self Care/Transcript"
										 class="category-page__member-thumbnail"
									></noscript>
								</a>
													</div>
						<a href="/wiki/Self_Care/Transcript" class="category-page__member-link" title="Self Care/Transcript">Self Care/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Shadowing_Glenn/Transcript" class="category-page__member-link" title="Shadowing Glenn/Transcript">Shadowing Glenn/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Shoplifter/Transcript" class="category-page__member-link" title="Shoplifter/Transcript">Shoplifter/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Shots_and_Salsa/Transcript" class="category-page__member-link" title="Shots and Salsa/Transcript">Shots and Salsa/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Spokesman_Scandal/Transcript" class="category-page__member-link" title="Spokesman Scandal/Transcript">Spokesman Scandal/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Spring_Cleaning/Transcript" class="category-page__member-link" title="Spring Cleaning/Transcript">Spring Cleaning/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Steps_Challenge/Transcript" class="category-page__member-link" title="Steps Challenge/Transcript">Steps Challenge/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Strike/Transcript" class="category-page__member-link" title="Strike/Transcript">Strike/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Super_Hot_Store/Transcript" class="category-page__member-link" title="Super Hot Store/Transcript">Super Hot Store/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					T				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Target/Transcript" class="category-page__member-link" title="Target/Transcript">Target/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																						<a href="/wiki/Testimonials/Transcript" title="Testimonials/Transcript">
									<img src="https://static.wikia.nocookie.net/superstore-nbc/images/8/8a/NUP_188090_0178.jpeg/revision/latest/smart/width/40/height/30?cb=20190928141833"
										 data-src="https://static.wikia.nocookie.net/superstore-nbc/images/8/8a/NUP_188090_0178.jpeg/revision/latest/smart/width/40/height/30?cb=20190928141833"
										 alt="Testimonials/Transcript"
										 class="category-page__member-thumbnail "
										 onload=""
									>
									<noscript><img src="https://static.wikia.nocookie.net/superstore-nbc/images/8/8a/NUP_188090_0178.jpeg/revision/latest/smart/width/40/height/30?cb=20190928141833"
										 alt="Testimonials/Transcript"
										 class="category-page__member-thumbnail"
									></noscript>
								</a>
													</div>
						<a href="/wiki/Testimonials/Transcript" class="category-page__member-link" title="Testimonials/Transcript">Testimonials/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Tornado/Transcript" class="category-page__member-link" title="Tornado/Transcript">Tornado/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Town_Hall/Transcript" class="category-page__member-link" title="Town Hall/Transcript">Town Hall/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Toxic_Work_Environment/Transcript" class="category-page__member-link" title="Toxic Work Environment/Transcript">Toxic Work Environment/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																						<a href="/wiki/Toy_Drive" title="Toy Drive">
									<img src="https://static.wikia.nocookie.net/superstore-nbc/images/3/3a/Break-time-superstore-s5e8.jpg/revision/latest/smart/width/40/height/30?cb=20191111144620"
										 data-src="https://static.wikia.nocookie.net/superstore-nbc/images/3/3a/Break-time-superstore-s5e8.jpg/revision/latest/smart/width/40/height/30?cb=20191111144620"
										 alt="Toy Drive"
										 class="category-page__member-thumbnail "
										 onload=""
									>
									<noscript><img src="https://static.wikia.nocookie.net/superstore-nbc/images/3/3a/Break-time-superstore-s5e8.jpg/revision/latest/smart/width/40/height/30?cb=20191111144620"
										 alt="Toy Drive"
										 class="category-page__member-thumbnail"
									></noscript>
								</a>
													</div>
						<a href="/wiki/Toy_Drive" class="category-page__member-link" title="Toy Drive">Toy Drive</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					V				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Valentine%27s_Day/Transcript" class="category-page__member-link" title="Valentine&#039;s Day/Transcript">Valentine&#039;s Day/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Video_Game_Release/Transcript" class="category-page__member-link" title="Video Game Release/Transcript">Video Game Release/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Viral_Video/Transcript" class="category-page__member-link" title="Viral Video/Transcript">Viral Video/Transcript</a>					</li>
							</ul>
		</div>
			<div class="category-page__members-wrapper">
							<div class="category-page__first-char">
					W				</div>
						<ul class="category-page__members-for-char">
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Wedding_Day_Sale/Transcript" class="category-page__member-link" title="Wedding Day Sale/Transcript">Wedding Day Sale/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Wellness_Fair/Transcript" class="category-page__member-link" title="Wellness Fair/Transcript">Wellness Fair/Transcript</a>					</li>
														<li class="category-page__member">
						<div class="category-page__member-left">
																				</div>
						<a href="/wiki/Workplace_Bullying/Transcript" class="category-page__member-link" title="Workplace Bullying/Transcript">Workplace Bullying/Transcript</a>					</li>
							</ul>
		</div>
	</div>
</div>				</div>
				<div class="page-footer">
					
					
												<div class="license-description">
		Community content is available under <a href="https://www.fandom.com/licensing">CC-BY-SA</a> unless otherwise noted.	</div>
					
									</div>
			</main>
							
<aside class="page__right-rail">
		
<div class="right-rail-wrapper WikiaRail">
	<div id="rail-boxad-wrapper"></div>
				<div id="WikiaRail"></div>
		</div>
</aside>

					</div>
		
	<div class="bottom-ads-container">
		<div class="ad-slot-placeholder bottom-leaderboard is-loading"></div>
		<div class="ae-translatable-label" data-key="advertisement">Advertisement</div>
	</div>
			</div>
			<footer class="global-footer">
	<div class="global-footer__content">
		<div>
			<h2 class="global-footer__header">
				<a href="https://www.fandom.com/"
				   data-tracking-label="logo"
				   title="Fandom"
				   aria-label="Fandom homepage"
				>
					<svg class="global-footer__header-logo"><use xlink:href="#wds-brand-fandom-logo-light"></use></svg>				</a>
			</h2>
			<section class="global-footer__section global-footer__section-fandom-overview">
			<h3 class="global-footer__section-header">Explore properties</h3>
	
	
	
			<ul class="global-footer__links">
							<li>
					<a href="https://www.fandom.com/"
					   class="global-footer__link"
					   data-tracking-label="explore.fandom"
					   aria-label=""
					>
						Fandom					</a>
				</li>
							<li>
					<a href="https://www.dndbeyond.com/"
					   class="global-footer__link"
					   data-tracking-label="explore.dnd-beyond"
					   aria-label=""
					>
						D&D Beyond					</a>
				</li>
							<li>
					<a href="https://www.cortexrpg.com/"
					   class="global-footer__link"
					   data-tracking-label="explore.cortexrpg"
					   aria-label=""
					>
						Cortex RPG					</a>
				</li>
							<li>
					<a href="https://www.muthead.com/"
					   class="global-footer__link"
					   data-tracking-label="explore.muthead"
					   aria-label=""
					>
						Muthead					</a>
				</li>
							<li>
					<a href="https://www.futhead.com/"
					   class="global-footer__link"
					   data-tracking-label="explore.futhead"
					   aria-label=""
					>
						Futhead					</a>
				</li>
							<li>
					<a href="https://www.fanatical.com/"
					   class="global-footer__link"
					   data-tracking-label="explore.fanatical"
					   aria-label=""
					>
						Fanatical					</a>
				</li>
					</ul>
	</section>
			<section class="global-footer__section global-footer__section-social-links">
			<h3 class="global-footer__section-header">Follow Us</h3>
	
	
	
			<ul class="global-footer__links">
							<li>
					<a href="https://www.facebook.com/getfandom"
					   class="global-footer__link"
					   data-tracking-label="follow-us.facebook"
					   aria-label="Follow Fandom on Facebook"
					>
						<svg class="global-footer__link-icon wds-icon wds-icon-small"><use xlink:href="#wds-icons-facebook"></use></svg>					</a>
				</li>
							<li>
					<a href="https://twitter.com/getfandom"
					   class="global-footer__link"
					   data-tracking-label="follow-us.twitter"
					   aria-label="Follow Fandom on Twitter"
					>
						<svg class="global-footer__link-icon wds-icon wds-icon-small"><use xlink:href="#wds-icons-twitter"></use></svg>					</a>
				</li>
							<li>
					<a href="https://www.youtube.com/fandomentertainment"
					   class="global-footer__link"
					   data-tracking-label="follow-us.youtube"
					   aria-label="Follow Fandom on Youtube"
					>
						<svg class="global-footer__link-icon wds-icon wds-icon-small"><use xlink:href="#wds-icons-youtube"></use></svg>					</a>
				</li>
							<li>
					<a href="https://www.instagram.com/getfandom/"
					   class="global-footer__link"
					   data-tracking-label="follow-us.instagram"
					   aria-label="Follow Fandom on Instagram"
					>
						<svg class="global-footer__link-icon wds-icon wds-icon-small"><use xlink:href="#wds-icons-instagram"></use></svg>					</a>
				</li>
							<li>
					<a href="https://www.linkedin.com/company/157252"
					   class="global-footer__link"
					   data-tracking-label="follow-us.linkedin"
					   aria-label="Follow Fandom on LinkedIn"
					>
						<svg class="global-footer__link-icon wds-icon wds-icon-small"><use xlink:href="#wds-icons-linkedin"></use></svg>					</a>
				</li>
					</ul>
	</section>
		</div>
		<div>
			<section class="global-footer__section global-footer__section-site-overview">
			<h3 class="global-footer__section-header">Overview</h3>
	
	
	
			<ul class="global-footer__links">
							<li>
					<a href="https://www.fandom.com/what-is-fandom"
					   class="global-footer__link"
					   data-tracking-label="company-overview.what-is-fandom"
					   aria-label=""
					>
						What is Fandom?					</a>
				</li>
							<li>
					<a href="https://www.fandom.com/about"
					   class="global-footer__link"
					   data-tracking-label="company-overview.about"
					   aria-label=""
					>
						About					</a>
				</li>
							<li>
					<a href="https://www.fandom.com/careers"
					   class="global-footer__link"
					   data-tracking-label="company-overview.careers"
					   aria-label=""
					>
						Careers					</a>
				</li>
							<li>
					<a href="https://www.fandom.com/press"
					   class="global-footer__link"
					   data-tracking-label="company-overview.press"
					   aria-label=""
					>
						Press					</a>
				</li>
							<li>
					<a href="https://www.fandom.com/about#contact"
					   class="global-footer__link"
					   data-tracking-label="company-overview.contact"
					   aria-label=""
					>
						Contact					</a>
				</li>
							<li>
					<a href="https://www.fandom.com/terms-of-use"
					   class="global-footer__link"
					   data-tracking-label="site-overview.terms-of-use"
					   aria-label=""
					>
						Terms of Use					</a>
				</li>
							<li>
					<a href="https://www.fandom.com/privacy-policy"
					   class="global-footer__link"
					   data-tracking-label="site-overview.privacy-policy"
					   aria-label=""
					>
						Privacy Policy					</a>
				</li>
							<li>
					<a href="//community.fandom.com/Sitemap"
					   class="global-footer__link"
					   data-tracking-label="site-overview.global-sitemap"
					   aria-label=""
					>
						Global Sitemap					</a>
				</li>
							<li>
					<a href="/wiki/Local_Sitemap"
					   class="global-footer__link"
					   data-tracking-label="site-overview.local-sitemap"
					   aria-label=""
					>
						Local Sitemap					</a>
				</li>
					</ul>
	</section>
		</div>
		<div>
			<section class="global-footer__section global-footer__section-community">
			<h3 class="global-footer__section-header">Community</h3>
	
	
	
			<ul class="global-footer__links">
							<li>
					<a href="//community.fandom.com/wiki/Community_Central"
					   class="global-footer__link"
					   data-tracking-label="community.community-central"
					   aria-label=""
					>
						Community Central					</a>
				</li>
							<li>
					<a href="https://fandom.zendesk.com/"
					   class="global-footer__link"
					   data-tracking-label="community.support"
					   aria-label=""
					>
						Support					</a>
				</li>
							<li>
					<a href="//community.fandom.com/wiki/Help:Contents"
					   class="global-footer__link"
					   data-tracking-label="community.help"
					   aria-label=""
					>
						Help					</a>
				</li>
							<li>
					<a href="https://www.fandom.com/do-not-sell-my-info"
					   class="global-footer__link"
					   data-tracking-label="community.usp-do-not-sell"
					   aria-label=""
					>
						Do Not Sell My Info					</a>
				</li>
					</ul>
	</section>
			<section class="global-footer__section global-footer__section-advertise">
			<h3 class="global-footer__section-header">Advertise</h3>
	
	
	
			<ul class="global-footer__links">
							<li>
					<a href="https://about.fandom.com/mediakit"
					   class="global-footer__link"
					   data-tracking-label="advertise.media-kit"
					   aria-label=""
					>
						Media Kit					</a>
				</li>
							<li>
					<a href="https://www.fandomatic.com"
					   class="global-footer__link"
					   data-tracking-label="advertise.fandomatic"
					   aria-label=""
					>
						Fandomatic					</a>
				</li>
							<li>
					<a href="https://about.fandom.com/mediakit#contact"
					   class="global-footer__link"
					   data-tracking-label="advertise.contact"
					   aria-label=""
					>
						Contact					</a>
				</li>
					</ul>
	</section>
		</div>
		<div>
			<section class="global-footer__section global-footer__section-fandom-apps">
			<h3 class="global-footer__section-header">Fandom Apps</h3>
	
			Take your favorite fandoms with you and never miss a beat.	
	
	</section>
			<section class="global-footer__section global-footer__section-fandom-stores">
	
	
			<svg class="global-footer__icon"><use xlink:href="#wds-brand-fandom-logo-store"></use></svg>	
			<ul class="global-footer__links">
							<li>
					<a href="https://apps.apple.com/us/app/fandom-videos-news-reviews/id1230063803"
					   class="global-footer__link"
					   data-tracking-label="community-apps.app-store"
					   aria-label="Fandom&#039;s Apple Store"
					>
						<svg class="global-footer__link-icon wds-icon wds-icon-small"><use xlink:href="#wds-brand-other-appstore"></use></svg>					</a>
				</li>
							<li>
					<a href="https://play.google.com/store/apps/details?id=com.fandom.app&referrer=utm_source%3Dwikia%26utm_medium%3Dglobalfooter"
					   class="global-footer__link"
					   data-tracking-label="community-apps.google-play"
					   aria-label="Fandom&#039;s Google Play"
					>
						<svg class="global-footer__link-icon wds-icon wds-icon-small"><use xlink:href="#wds-brand-other-googleplay"></use></svg>					</a>
				</li>
					</ul>
	</section>
			<section class="global-footer__section global-footer__section-ddb-stores">
	
	
			<svg class="global-footer__icon"><use xlink:href="#wds-brand-ddb-logo-store"></use></svg>	
			<ul class="global-footer__links">
							<li>
					<a href="https://apps.apple.com/us/app/id1501810129"
					   class="global-footer__link"
					   data-tracking-label="community-apps.app-store-ddb"
					   aria-label="D&amp;D Beyond&#039;s Apple Store"
					>
						<svg class="global-footer__link-icon wds-icon wds-icon-small"><use xlink:href="#wds-brand-other-appstore"></use></svg>					</a>
				</li>
							<li>
					<a href="https://play.google.com/store/apps/details?id=com.fandom.playercompanion&referrer=utm_source%3Dwikia%26utm_medium%3Dglobalfooter"
					   class="global-footer__link"
					   data-tracking-label="community-apps.google-play-ddb"
					   aria-label="D&amp;D Beyond&#039;s Google Play"
					>
						<svg class="global-footer__link-icon wds-icon wds-icon-small"><use xlink:href="#wds-brand-other-googleplay"></use></svg>					</a>
				</li>
					</ul>
	</section>
		</div>
	</div>
	<div class="global-footer__bottom">
		<div>Superstore Wiki is a FANDOM TV Community.</div>
					<div>
				<a href="https://superstore-nbc.fandom.com/wiki/Category:Transcripts?title=Category%3ATranscripts&mobileaction=toggle_view_mobile" class="global-footer__switch-view global-footer__switch-to-mobile">
					View Mobile Site				</a>
			</div>
			</div>
</footer>
	</div>

<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.001","walltime":"0.001","ppvisitednodes":{"value":1,"limit":1000000},"ppgeneratednodes":{"value":0,"limit":1000000},"postexpandincludesize":{"value":0,"limit":2097152},"templateargumentsize":{"value":0,"limit":2097152},"expansiondepth":{"value":1,"limit":40},"expensivefunctioncount":{"value":0,"limit":100},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":0,"limit":5000000},"timingprofile":["100.00%    0.000      1 -total"]},"cachereport":{"timestamp":"20220404180835","ttl":1209600,"transientcontent":false}}});});</script>
<script defer="" src="https://www.fastly-insights.com/static/scout.js?k=17272cd8-82ee-4eb5-b5a3-b3cd5403f7c5"></script>
<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":191});});</script><div id="WikiaBar">
	<div id="WikiaBarWrapper" class="WikiaBarWrapper hidden">
		<div class="wikia-bar wikia-bar-anon">
				<a class="wikiabar-button" href="https://bit.ly/FandomIG" data-index="0">
		<span>Follow on IG</span>
	</a>
	<a class="wikiabar-button" href="https://bit.ly/WBEmailCap" data-index="1">
		<span>Newsletter</span>
	</a>
	<a class="wikiabar-button" href="https://bit.ly/FanLabWikiBar" data-index="2">
		<span>Join Fan Lab</span>
	</a>
<div
	class="message"
	data-messagetooltip="Click here for more information!"
	data-wikiabarcontent="[{&quot;text&quot;:&quot;Bingebot: Find a new show to watch in 30 seconds&quot;,&quot;href&quot;:&quot;http:\/\/bit.ly\/Binge30&quot;},{&quot;text&quot;:&quot;Bingebot: Find a new show to watch in 30 seconds&quot;,&quot;href&quot;:&quot;http:\/\/bit.ly\/Binge30&quot;},{&quot;text&quot;:&quot;Bingebot: Find a new show to watch in 30 seconds&quot;,&quot;href&quot;:&quot;http:\/\/bit.ly\/Binge30&quot;},{&quot;text&quot;:&quot;Bingebot: Find a new show to watch in 30 seconds&quot;,&quot;href&quot;:&quot;http:\/\/bit.ly\/Binge30&quot;},{&quot;text&quot;:&quot;Bingebot: Find a new show to watch in 30 seconds&quot;,&quot;href&quot;:&quot;http:\/\/bit.ly\/Binge30&quot;}]"
></div>
			<a href="#" class="arrow" data-trigger="hover" data-tooltip="Collapse"
			   data-tooltipshow="Show">
				<svg class="wds-icon wds-icon-small close-icon"><use xlink:href="#wds-icons-close-small"></use></svg>			</a>
		</div>
	</div>

	<div class="WikiaBarCollapseWrapper" data-trigger="hover"
		 data-tooltip="Collapse">
		<div class="wikia-bar-collapse">
			<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" viewBox="0 0 24 24"
				 class="wds-icon wds-icon-small">
				<g clip-path="url(#wrench_clip0)">
					<path d="M23 4c-.265 0-.52.105-.707.293C22.105 4.48 22 4.735 22 5v2h-5V2h2c.265 0 .52-.105.707-.293C19.895 1.52 20 1.265 20 1c0-.265-.105-.52-.293-.707C19.52.105 19.265 0 19 0h-5c-.132 0-.262.024-.384.074-.122.05-.233.123-.326.216l-4 4c-.093.093-.166.204-.216.326C9.024 4.738 9 4.868 9 5v4.59l-7.71 7.7C.571 18.009.167 18.984.167 20c0 1.017.404 1.991 1.123 2.71.719.719 1.694 1.122 2.71 1.122s1.991-.403 2.71-1.122l7.7-7.71H19c.132 0 .262-.024.384-.074.122-.05.233-.123.326-.216l4-4c.093-.093.166-.204.216-.326.05-.122.075-.252.074-.384V5c0-.265-.105-.52-.293-.707C23.52 4.105 23.265 4 23 4zm-1 5.59L18.59 13H14c-.132 0-.262.024-.384.074-.122.05-.233.123-.326.216l-8 8c-.342.342-.806.534-1.29.534s-.948-.192-1.29-.534c-.342-.342-.534-.806-.534-1.29s.192-.948.534-1.29l8-8c.093-.093.166-.204.216-.326.05-.122.075-.252.074-.384V5.41L14.41 2H15v6c0 .265.105.52.293.707.187.188.442.293.707.293h6v.59z"/>
				</g>
				<defs>
					<clipPath id="wrench_clip0">
						<path fill="#fff" d="M0 0H24V24H0z"/>
					</clipPath>
				</defs>
			</svg>
		</div>
	</div>
</div>
</body></html>
"""

epSoup = BeautifulSoup(episodeDoc, 'html.parser')

urls = []
for a in epSoup.find_all('a', href=True, class_='category-page__member-link'):
    link = a['href']
    urls.append(link)


rows = []
for url in urls:
    print(url)
    # Gets the episode number from a different URL
    urlSplit = url.split('/')
    ep_doc = req.get('https://superstore-nbc.fandom.com/' + urlSplit[1] + '/' + urlSplit[2])
    S = BeautifulSoup(ep_doc.content, 'html.parser')
    dataDivs = S.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
    for div in dataDivs:
        if div.attrs['data-source'] == 'episode':
            episodeNumber = div.get_text().split('\n')[2]
        if div.attrs['data-source'] == 'season':
            seasonNumberText = div.get_text().split('\n')[2]
            numberMap = {
                'One': 1,
                '1': 1,
                'Two': 2,
                '2': 2,
                'Three': 3,
                '3': 3,
                'Four': 4,
                '4': 4,
                'Five': 5,
                '5': 5,
                'Six': 6,
                '6': 6
            }
            seasonNumber = numberMap[seasonNumberText]

    html_doc = req.get('https://superstore-nbc.fandom.com' + url)
    if html_doc:
        S = BeautifulSoup(html_doc.content, 'html.parser')
        textDiv = S.find_all('div', class_='poem')
        for item in textDiv:
            text = item.get_text()
            lines = text.split('\n')
            for line in lines:
                lineSplit = line.split(':')
                if len(line) > 0 and len(lineSplit) == 2:
                    character = lineSplit[0].strip()
                    if '(' in character:
                        character = character.split('(')[0].strip()
                    if ',' in character:
                        character = character.split('(')
                    text = lineSplit[1].strip()
                    rows.append([character, text, seasonNumber, episodeNumber])

    else:
        print('Failed to get ' + url)

os.chdir('C:/workdir/visual-interfaces/Project3/data')

with open('showData.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(['Character', 'Line', 'Season', 'Episode'])
    for row in rows:
        writer.writerow(row)